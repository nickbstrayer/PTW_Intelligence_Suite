import streamlit as st

# Import pages (these execute immediately if they contain top-level Streamlit code)
import pages.ptw_calculator as ptw_calculator
import pages.ptw_calculator_full  # NOTE: no function call – the import runs the code
import pages.salary_estimator as salary_estimator
import pages.job_classifier as job_classifier
import pages.visual_dashboard as visual_dashboard

# Set up the main page
st.set_page_config(page_title="PTW Intelligence Suite", layout="wide")

st.sidebar.markdown("## 🔐 PTW Intelligence Suite")
page = st.sidebar.radio(
    "Navigate to:",
    (
        "🏠 Home",
        "📊 PTW Calculator",
        "📏 PTW Calculator – Full",
        "💰 Salary Estimator",
        "🤖 AI Job Classifier",
        "📊 Visual Summary Dashboard"
    )
)

# --- Main Page Logic ---
if page == "🏠 Home":
    st.title("🏠 Welcome to the PTW Intelligence Suite")
    st.markdown("""
        This suite helps simulate labor pricing, evaluate salary and win probabilities,
        classify roles with AI, and visualize trends to support Price-to-Win strategies.
    """)

elif page == "📊 PTW Calculator":
    ptw_calculator.render_ptw_calculator()

elif page == "📏 PTW Calculator – Full":
    # The code in pages.ptw_calculator_full runs on import
    pass

elif page == "💰 Salary Estimator":
    salary_estimator.render_salary_estimator()

elif page == "🤖 AI Job Classifier":
    job_classifier.render_job_classifier()

elif page == "📊 Visual Summary Dashboard":
    visual_dashboard.render_visual_dashboard()
