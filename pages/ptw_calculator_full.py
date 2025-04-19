import streamlit as st
from scripts.api_connectors import fetch_sam_details

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

# ✅ UPDATED CONTRACT TYPE DROPDOWN
contract_type = st.selectbox(
    "Contract Type",
    [
        "Full & Open",
        "SDVOSB",
        "WOSB",
        "HubZone",
        "ANC",
        "Small Business Set Aside",  # ✅ newly added option
        "Other"
    ]
)

# --- Form Section 2: Labor Info ---
st.subheader("Labor Info")
labor_category = st.selectbox("Labor Category", ["Program Manager", "Analyst", "Engineer", "Administrator", "Other"])
base_salary = st.number_input("Base Salary Estimate ($)", min_value=0.0, format="%.2f")
bill_low = st.number_input("Bill Rate – Low ($)", min_value=0.0, format="%.2f")
bill_mid = st.number_input("Bill Rate – Mid ($)", min_value=0.0, format="%.2f")
bill_high = st.number_input("Bill Rate – High ($)", min_value=0.0, format="%.2f")

# ✅ You can continue with Contracting Context, Modifiers, Benchmarking, etc.
