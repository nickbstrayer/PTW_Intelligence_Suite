import streamlit as st
from pages import ptw_calculator, ptw_calculator_full, salary_estimator, visual_dashboard
from pages.ptw_calculator_full import render_ptw_calculator

# Sidebar UI
st.sidebar.title("🛠 PTW Intelligence Suite")
page = st.sidebar.radio("Navigate to:", (
    "🏠 Home",
    "📊 PTW Calculator",
    "📌 PTW Calculator – Full",
    "💰 Salary Estimator",
    "🤖 AI Job Classifier",
    "📈 Visual Summary Dashboard"
))

# Page Routing
if page == "🏠 Home":
    st.title("Welcome to the PTW Intelligence Suite")
    st.markdown("Select a module from the sidebar to begin.")
elif page == "📊 PTW Calculator":
    ptw_calculator.main()
elif page == "📌 PTW Calculator – Full":
    render_ptw_calculator()
elif page == "💰 Salary Estimator":
    salary_estimator.main()
elif page == "🤖 AI Job Classifier":
    st.markdown("🔧 Job Classifier will be activated soon.")
elif page == "📈 Visual Summary Dashboard":
    visual_dashboard.main()
