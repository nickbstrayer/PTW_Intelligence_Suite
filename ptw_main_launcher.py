import sys
import os
import streamlit as st

# Ensure the 'scripts' folder is included in Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'scripts'))

from streamlit_auth import initialize_session_state, render_auth_page

# Initialize user session
initialize_session_state()

# 🚪 Authentication Gate
if not st.session_state.get("is_authenticated"):
    render_auth_page()

else:
    # Sidebar navigation
    st.sidebar.title("🔐 PTW Intelligence Suite")
    selection = st.sidebar.radio("Navigate to:", [
        "🏠 Home",
        "🧮 PTW Calculator",
        "📥 Salary Estimator",
        "🤖 AI Job Classifier",
        "📊 Visual Summary Dashboard"
    ])

    # Load appropriate tool
    if selection == "🏠 Home":
        st.title("🏠 Welcome to the PTW Intelligence Suite")
        st.markdown("This tool helps you analyze, simulate, and optimize contract pricing strategies.")
        st.success(f"You are logged in as **{st.session_state.login_email}**")

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
