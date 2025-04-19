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

    agency_name = ""
    contract_title = ""
    published_date = ""
    due_date = ""
    competition = ""
    estimated_value = 0.0
    set_aside = ""
    psc = ""
    naics = ""
    pop = ""
    description = ""

    if fetch_button and solicitation_number:
        sam_data = fetch_sam_details(solicitation_number)
        agency_name = sam_data.get("agency_name", "")
        contract_title = sam_data.get("title", "")
        published_date = sam_data.get("published_date", "")
        due_date = sam_data.get("due_date", "")
        competition = sam_data.get("competition", "")
        estimated_value = sam_data.get("estimated_value", 0.0)
        set_aside = sam_data.get("set_aside", "")
        psc = sam_data.get("psc", "")
        naics = sam_data.get("naics", "")
        pop = sam_data.get("pop", "")
        description = sam_data.get("description", "")

    agency_name = st.text_input("Agency Name or Sub-agency", value=agency_name, key="agency_input")
    contract_title = st.text_input("Contract Title", value=contract_title, key="title_input")
    st.text_input("Solicitation Number", value=solicitation_number, key="sol_number_final")
    st.text_input("Published Date", value=published_date, key="published_input")
    st.text_input("Due Date", value=due_date, key="due_input")
    st.text_input("Competition Type", value=competition, key="competition_input")
    contract_value = st.number_input("Contract Estimated Value ($)", value=estimated_value, min_value=0.0, format="%.2f")
    st.text_input("Set-Aside Type", value=set_aside, key="setaside_input")
    st.text_input("Product Service Code (PSC)", value=psc, key="psc_input")
    st.text_input("NAICS Code", value=naics, key="naics_input")
    st.text_input("Place of Performance", value=pop, key="pop_input")
    st.text_area("Description", value=description, key="description_input")

    st.markdown("### 📌 Labor Info")
    labor_category = st.selectbox("Labor Category", ["Program Manager", "Analyst", "Engineer", "Administrator", "Other"])
    base_salary = st.number_input("Base Salary Estimate ($)", min_value=0.0, format="%.2f")
    bill_low = st.number_input("Bill Rate – Low ($)", min_value=0.0, format="%.2f")
    bill_mid = st.number_input("Bill Rate – Mid ($)", min_value=0.0, format="%.2f")
    bill_high = st.number_input("Bill Rate – High ($)", min_value=0.0, format="%.2f")

    st.success("Section loaded successfully – more sections will appear as we continue integration.")

# IMPORTANT: Add this call to render the page when loaded directly
render_ptw_calculator()
