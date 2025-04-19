import streamlit as st
from pages import ptw_calculator, salary_estimator, visual_dashboard, job_classifier
from pages import ptw_calculator_full  # ✅ This connects the full PTW calculator

st.set_page_config(page_title="PTW Intelligence Suite", layout="wide")

# Sidebar Navigation
st.sidebar.markdown("### 🧭 PTW Intelligence Suite")
page = st.sidebar.radio("Navigate to:", [
    "🏠 Home", 
    "📊 PTW Calculator", 
    "📈 Salary Estimator",
    "🤖 AI Job Classifier",
    "📊 Visual Summary Dashboard",
    "PTW Calculator – Full"  # ✅ Make sure this is in the list
])

# Page Routing
if page == "🏠 Home":
    st.title("🏠 Welcome to the PTW Intelligence Suite")
    st.markdown("Use the navigation panel to access each module.")
elif page == "📊 PTW Calculator":
    ptw_calculator.render()
elif page == "📈 Salary Estimator":
    salary_estimator.render()
elif page == "🤖 AI Job Classifier":
    job_classifier.render()
elif page == "📊 Visual Summary Dashboard":
    visual_dashboard.render()
elif page == "PTW Calculator – Full":
    ptw_calculator_full.render_ptw_calculator()  # ✅ This renders the full version
