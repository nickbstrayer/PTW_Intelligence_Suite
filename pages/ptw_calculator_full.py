import streamlit as st
import pandas as pd
import numpy as np
import requests
import json

def render_ptw_calculator():
    st.markdown("## 🔢 Full PTW Calculator")

    with st.form("ptw_form"):
        st.subheader("Agency and Contract Info")
        agency = st.text_input("Agency Name or Sub-agency")
        contract_title = st.text_input("Contract Title")
        solicitation_number = st.text_input("Solicitation Number")
        contract_value = st.number_input("Contract Estimated Value ($)", step=1000.0)
        contract_type = st.selectbox("Contract Type", ["Full & Open", "SDVOSB", "WOSB", "HubZone", "ANC", "Other"])

        st.subheader("Labor Info")
        labor_category = st.selectbox("Labor Category", ["Program Manager", "Analyst", "Engineer", "Support Staff"])
        base_salary = st.number_input("Base Salary Estimate ($)", step=1000.0)
        bill_low = st.number_input("Bill Rate - Low ($)", step=100.0)
        bill_mid = st.number_input("Bill Rate - Mid ($)", step=100.0)
        bill_high = st.number_input("Bill Rate - High ($)", step=100.0)

        st.subheader("Contracting Context")
        eval_category = st.selectbox("Evaluation Category", ["Best Value", "LPTA", "Undefined"])
        pricing_scenario = st.selectbox("Pricing Scenario", ["New Requirement", "Recompete"])

        st.subheader("Modifiers")
        job_intensity = st.selectbox("Job Description Intensity", ["High", "Medium", "Low", "Unknown"])
        specialized = st.selectbox("Specialized Requirement?", ["Yes", "No"])
        political_modifier = st.selectbox("Political Trend Modifier", ["Expansionary (+3%)", "Neutral (0%)", "Contractionary (-3%)"])

        st.subheader("Benchmarking")
        historical_value = st.number_input("Historical Contract Value (if any) ($)", step=1000.0)
        gsa_benchmark = st.number_input("Comparable Rate Benchmark (GSA, etc.) ($)", step=10.0)

        submitted = st.form_submit_button("Calculate PTW")

    if submitted:
        st.subheader("Computed Results")
        def modifier_factor(intensity, specialized, politics):
            factor = 1.0
            if intensity == "High":
                factor += 0.05
            elif intensity == "Low":
                factor -= 0.03

            if specialized == "Yes":
                factor += 0.04

            if "Expansionary" in politics:
                factor += 0.03
            elif "Contractionary" in politics:
                factor -= 0.03

            return factor

        mod = modifier_factor(job_intensity, specialized, political_modifier)

        adj_low = round(bill_low * mod, 2)
        adj_mid = round(bill_mid * mod, 2)
        adj_high = round(bill_high * mod, 2)

        if gsa_benchmark > 0:
            variance = round(((bill_mid - gsa_benchmark) / gsa_benchmark) * 100, 2)
        else:
            variance = "N/A"

        def win_prob(rate, benchmark):
            if benchmark <= 0:
                return 0.0
            diff = rate - benchmark
            prob = 100 - (diff / benchmark * 100)
            return max(min(round(prob, 2), 100), 0)

        win_low = win_prob(adj_low, gsa_benchmark)
        win_mid = win_prob(adj_mid, gsa_benchmark)
        win_high = win_prob(adj_high, gsa_benchmark)

        best_rate = adj_low if win_low >= win_mid and win_low >= win_high else (
            adj_mid if win_mid >= win_high else adj_high)
        best_win = max(win_low, win_mid, win_high)

        st.metric("Adjusted Rate - Low", f"${adj_low}")
        st.metric("Adjusted Rate - Mid", f"${adj_mid}")
        st.metric("Adjusted Rate - High", f"${adj_high}")

        st.metric("Win Probability - Low", f"{win_low}%")
        st.metric("Win Probability - Mid", f"{win_mid}%")
        st.metric("Win Probability - High", f"{win_high}%")

        st.success(f"Recommended PTW Rate: ${best_rate} with {best_win}% chance to win")

        st.markdown("### Justification Notes")
        st.write(f"Rate adjusted using {job_intensity} job intensity, {'specialized' if specialized == 'Yes' else 'non-specialized'} role, and a {political_modifier} market.")
        st.write(f"Variance from benchmark: {variance if variance != 'N/A' else 'Not available'}%")
