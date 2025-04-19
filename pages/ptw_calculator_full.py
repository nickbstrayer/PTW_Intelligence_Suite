import streamlit as st
from scripts.api_connectors import fetch_sam_details

def render_ptw_calculator():
    st.set_page_config(page_title="PTW Calculator – Full", layout="wide")

    st.markdown("""
        <h1 style='display: flex; align-items: center;'>
            <span style='font-size: 32px; margin-right: 10px;'>🔢</span> Full PTW Calculator
        </h1>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # --- Form Section 1: Agency and Contract Info ---
    st.subheader("Agency and Contract Info")

    with st.form("sam_lookup"):
        solicitation_number = st.text_input("Solicitation Number", key="sam_lookup_input")
        fetch_button = st.form_submit_button("🔍 Pull from SAM.gov")

    if fetch_button and solicitation_number:
        sam_data = fetch_sam_details(solicitation_number)
        agency_name = sam_data.get("agency_name", "")
        contract_title = sam_data.get("title", "")
    else:
        agency_name = ""
        contract_title = ""

    agency_name = st.text_input("Agency Name or Sub-agency", value=agency_name, key="agency_input")
    contract_title = st.text_input("Contract Title", value=contract_title, key="title_input")
    st.text_input("Solicitation Number", value=solicitation_number, key="sol_number_final")
    contract_value = st.number_input("Contract Estimated Value ($)", min_value=0.0, format="%.2f")
    contract_type = st.selectbox(
        "Contract Type",
        ["Full & Open", "Small Business Set Aside", "SDVOSB", "WOSB", "HubZone", "ANC", "Other"]
    )

    # --- Section 2: Labor Info ---
    st.markdown("### 📌 Labor Info")
    labor_category = st.selectbox("Labor Category", ["Program Manager", "Analyst", "Engineer", "Administrator", "Other"])
    base_salary = st.number_input("Base Salary Estimate ($)", min_value=0.0, format="%.2f")
    bill_low = st.number_input("Bill Rate – Low ($)", min_value=0.0, format="%.2f")
    bill_mid = st.number_input("Bill Rate – Mid ($)", min_value=0.0, format="%.2f")
    bill_high = st.number_input("Bill Rate – High ($)", min_value=0.0, format="%.2f")

    # --- Section 3: Contracting Context ---
    st.markdown("### 📁 Contracting Context")

    evaluation_category = st.selectbox(
        "Evaluation Category",
        ["Best Value", "Lowest Price Technically Acceptable (LPTA)", "Tradeoff", "Other"]
    )

    pricing_scenario = st.selectbox(
        "Pricing Scenario",
        ["New Requirement", "Incumbent Contractor", "Follow-on / Recompete", "Bridge / Extension", "Other"]
    )

    job_description_intensity = st.selectbox(
        "Job Description Intensity",
        ["Low", "Medium", "High", "Unknown"]
    )

    st.success("Contracting context loaded successfully.")

# IMPORTANT: Add this call to render the page when loaded directly
render_ptw_calculator()
