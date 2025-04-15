import streamlit as st
import sys, os
sys.path.append(os.path.abspath("scripts"))
from scripts.streamlit_auth import initialize_session_state, render_auth_page

# Initialize session state
initialize_session_state()

# Authenticated Routing
if not st.session_state.get("is_authenticated"):
    render_auth_page()
else:
    st.sidebar.title("🔐 PTW Intelligence Suite")
    selection = st.sidebar.radio("Navigate to:", [
        "🏠 Home", 
        "🧮 PTW Calculator", 
        "📥 Salary Estimator", 
        "🤖 AI Job Classifier", 
        "📊 Visual Summary Dashboard"
    ])

    if selection == "🏠 Home":
        st.title("🏠 Welcome to the PTW Intelligence Suite")
        st.write("Navigate from the left to access powerful pricing, salary, and AI tools.")
        st.success("You are logged in as: **{}**".format(st.session_state.login_email))

    elif selection == "🧮 PTW Calculator":
        import pages.ptw_calculator as ptw
        ptw.render()

    elif selection == "📥 Salary Estimator":
        import pages.salary_estimator as salary
        salary.render()

    elif selection == "🤖 AI Job Classifier":
        import pages.job_classifier as classifier
        classifier.render()

    elif selection == "📊 Visual Summary Dashboard":
        import pages.visual_dashboard as dashboard
        dashboard.render()
