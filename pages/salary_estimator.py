import streamlit as st
import pandas as pd
import joblib
import os

def render():
    st.markdown("### 💰 Salary Estimator")
    st.write("Estimate salary based on role, education, location, and experience.")

    # ✅ Use explicit relative path to load model
    model_path = os.path.join("models", "salary_estimator_model.pkl")
    assert os.path.exists(model_path), f"Model file not found at path: {model_path}"

    model = joblib.load(model_path)

    # Input form
    with st.form("salary_form"):
        st.write("Enter your job details:")
        role = st.selectbox("Job Role", ["Software Engineer", "Data Analyst", "Project Manager", "Consultant"])
        education = st.selectbox("Education Level", ["High School", "Bachelor's", "Master's", "PhD"])
        experience = st.slider("Years of Experience", 0, 30, 5)
        location = st.selectbox("Location", ["Remote", "Urban", "Suburban", "Rural"])

        submitted = st.form_submit_button("Estimate Salary")

    if submitted:
        # Convert inputs to features — update this logic to match model training
        features = pd.DataFrame([{
            "role": role,
            "education": education,
            "experience": experience,
            "location": location
        }])

        # Optional preprocessing here if your model expects encoded values
        prediction = model.predict(features)[0]
        st.success(f"Estimated Salary: ${prediction:,.2f}")
