import streamlit as st
from pages import ptw_calculator, ptw_calculator_full, salary_estimator, visual_dashboard

st.set_page_config(page_title="PTW Intelligence Suite", layout="wide")

st.sidebar.title("🛡️ PTW Intelligence Suite")
page = st.sidebar.radio("Navigate to:", (
    "🏠 Home",
    "📊 PTW Calculator",
    "📉 PTW Calculator – Full",
    "💰 Salary Estimator",
    "🤖 AI Job Classifier",
    "📊 Visual Summary Dashboard"
))

if page == "🏠 Home":
    st.markdown("""
        <h1 style='text-align: center;'>PTW Intelligence Suite</h1>
        <p style='text-align: center;'>Use the sidebar to navigate between modules for price-to-win analysis, salary benchmarking, and job classification.</p>
    """, unsafe_allow_html=True)

elif page == "📊 PTW Calculator":
    ptw_calculator.render_ptw_calculator()

elif page == "📉 PTW Calculator – Full":
    ptw_calculator_full.render_ptw_calculator()

elif page == "💰 Salary Estimator":
    salary_estimator.render_salary_estimator()

elif page == "🤖 AI Job Classifier":
    st.warning("AI Job Classifier is not yet implemented.")

elif page == "📊 Visual Summary Dashboard":
    visual_dashboard.render_dashboard()
