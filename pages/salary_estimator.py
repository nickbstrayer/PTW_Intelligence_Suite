import streamlit as st
import joblib
import pandas as pd

def render():
    st.header("📥 Salary Estimator")
    st.write("Estimate salary based on role, education, location, and experience.")

    model = joblib.load("salary_estimator_model.pkl")

    job_title = st.selectbox("Job Title", ["Logistics Analyst IV", "Program Manager", "Administrative Assistant"])
    education = st.selectbox("Education", ["High School", "Associate's", "Bachelor's"])
    experience = st.slider("Experience (years)", 0, 30, 5)
    clearance = st.selectbox("Clearance", ["None", "Secret"])
    location = st.selectbox("Location", ["Fort Detrick, MD", "Remote", "Germany"])

    if st.button("Estimate Salary"):
        input_df = pd.DataFrame([{
            "Job Title": job_title,
            "Education Requirement": education,
            "Years of Experience": experience,
            "Clearance Required": clearance,
            "Location": location
        }])
        prediction = model.predict(input_df)[0]
        st.success(f"Estimated Salary: ${prediction:,.2f}")
