# pages/salary_estimator.py

import streamlit as st
import pandas as pd
import joblib
import os

def render():
    st.markdown("### 💰 Salary Estimator")
    st.write("Estimate salary based on role, education, location, and experience.")

    # Define inputs
    role = st.text_input("Job Role", "Data Scientist")
    education = st.selectbox("Education Level", ["High School", "Associate", "Bachelor's", "Master's", "PhD"])
    location = st.text_input("Location", "Washington, DC")
    experience = st.slider("Years of Experience", 0, 40, 5)

    # Load the model safely from correct directory
    try:
        model_path = os.path.join("models", "salary_estimator_model.pkl")
        model = joblib.load(model_path)
    except FileNotFoundError:
        st.error(f"Model file not found at `{model_path}`. Please ensure the model is correctly placed in the `/models` directory.")
        return

    # Create feature dataframe (must match the format the model was trained on)
    input_df = pd.DataFrame([{
        "role": role,
        "education": education,
        "location": location,
        "experience": experience
    }])

    # Predict salary
    try:
        predicted_salary = model.predict(input_df)[0]
        st.success(f"💵 Estimated Salary: ${predicted_salary:,.2f}")
    except Exception as e:
        st.error(f"Prediction failed. Please check model compatibility.\n\nError: {e}")
