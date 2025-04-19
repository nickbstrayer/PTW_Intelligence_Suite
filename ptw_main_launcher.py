import streamlit as st
from pages import ptw_calculator, ptw_calculator_full, salary_estimator, visual_dashboard

st.set_page_config(
    page_title="PTW Intelligence Suite",
    page_icon="🧠",
    layout="wide"
)

# Sidebar
with st.sidebar:
    st.markdown("### 🔐 PTW Intelligence Suite")
    st.radio("Navigate to:", [
        "🏠 Home",
        "📊 PTW Calculator",
        "📈 PTW Calculator – Full",
        "💰 Salary Estimator",
        # "🤖 AI Job Classifier",  # ← DISABLED to avoid spaCy crash
        "📊 Visual Summary Dashboard"
    ], key="page_selector")

# Main Page Routing
page = st.session_state.page_selector

if page == "🏠 Home":
    st.markdown("## 🧠 PTW Intelligence Suite")
    st.write("""
        This suite provides government contractors and pricing teams with data-driven tools 
        to estimate competitive labor rates, understand win probabilities, and generate 
        justifications to support pricing strategies.
    """)
    st.info("Select a tool from the left to begin.")

elif page == "📊 PTW Calculator":
    ptw_calculator.render()

elif page == "📈 PTW Calculator – Full":
    ptw_calculator_full.render_ptw_calculator()

elif page == "💰 Salary Estimator":
    salary_estimator.render()

# elif page == "🤖 AI Job Classifier":
#     job_classifier.render()  # ← DISABLED due to spaCy incompatibility

elif page == "📊 Visual Summary Dashboard":
    visual_dashboard.render()
