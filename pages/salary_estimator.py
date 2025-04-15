# pages/salary_estimator.py

import streamlit as st
import pandas as pd
import joblib
import os

def render():
    st.markdown("## 💰 Salary Estimator")
    st.markdown("Estimate salary based on role, education, location, and experience.")

    # UI for input
    role = st.selectbox("Select Role", ["Data Analyst", "Software Engineer", "Project Manager", "Cybersecurity Specialist"])
    education = st.selectbox("Education Level", ["High School", "Associate", "Bachelor", "Master", "PhD"])
    location = st.selectbox("Location", ["Washington, DC", "New York, NY", "Austin, TX", "Remote"])
    years_exp = st.slider("Years of Experience", 0, 40, 5)

    # Build input dataframe
    input_data = pd.DataFrame([{
        "role": role,
        "education": education,
        "location": location,
        "years_exp": years_exp
    }])

    # Load model
    model_path = os.path.join("models", "salary_estimator_model.pkl")
    try:
        model = joblib.load(model_path)
        prediction = model.predict(input_data)[0]

        st.success(f"💵 Estimated Salary: **${prediction:,.0f}** per year")
    except FileNotFoundError:
        st.error(f"❌ Could not find model file at: `{model_path}`")
    except Exception as e:
        st.error(f"❌ Error during prediction: {e}")
