import streamlit as st
from pages import ptw_calculator, salary_estimator, visual_dashboard, job_classifier
from pages.ptw_calculator_full import render_ptw_calculator

# Sidebar navigation
st.sidebar.title("🔰 PTW Intelligence Suite")
page = st.sidebar.radio("Navigate to:", [
    "🏠 Home",
    "📊 PTW Calculator",
    "🧮 PTW Calculator – Full",
    "💰 Salary Estimator",
    "🤖 AI Job Classifier",
    "📊 Visual Summary Dashboard"
])

# Route to selected page
if page == "🏠 Home":
    st.title("Welcome to PTW Intelligence Suite")
    st.markdown("Use the navigation menu to access different modules for labor pricing, classification, dashboards, and more.")

elif page == "📊 PTW Calculator":
    ptw_calculator.main()

elif page == "🧮 PTW Calculator – Full":
    render_ptw_calculator()

elif page == "💰 Salary Estimator":
    salary_estimator.main()

elif page == "🤖 AI Job Classifier":
    job_classifier.main()

elif page == "📊 Visual Summary Dashboard":
    visual_dashboard.main()
