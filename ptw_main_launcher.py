import streamlit as st
import importlib.util
import os

# Dynamically load streamlit_auth from scripts/streamlit_auth.py
auth_path = os.path.join(os.path.dirname(__file__), "scripts", "streamlit_auth.py")
spec = importlib.util.spec_from_file_location("streamlit_auth", auth_path)
auth_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(auth_module)

# Call authentication functions
auth_module.initialize_session_state()

if not st.session_state.get("is_authenticated"):
    auth_module.render_auth_page()

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
