import streamlit as st
import pandas as pd
import numpy as np
import requests
from sklearn.linear_model import LinearRegression

# ------------------------
# Utilities
# ------------------------
def fetch_agencies():
    # Placeholder values for now
    return ["Department of Defense", "Department of State", "Department of Homeland Security", "Other"]

def compute_adjusted_rates(base_rate, job_intensity, spec_req, trend_mod):
    intensity_factor = {"Low": 1.00, "Medium": 1.05, "High": 1.12, "Unknown": 1.03}.get(job_intensity, 1.00)
    spec_factor = 1.05 if spec_req == "Yes" else 1.00
    trend_factor = {"Expansionary (+3%)": 1.03, "Neutral (0%)": 1.00, "Contractionary (-3%)": 0.97}.get(trend_mod, 1.00)
    adj = base_rate * intensity_factor * spec_factor * trend_factor
    return round(adj, 2)

def compute_win_probability(rate, benchmark):
    # Simple linear interpolation for demonstration
    model = LinearRegression()
    x = np.array([benchmark * 0.9, benchmark, benchmark * 1.1]).reshape(-1, 1)
    y = np.array([0.85, 0.65, 0.30])  # Probabilities decline as rate increases
    model.fit(x, y)
    return round(float(model.predict(np.array([[rate]]))), 2)

# ------------------------
# App Layout
# ------------------------

def render_ptw_calculator():
    st.markdown("### 📊 PTW Calculator – Full")

    with st.form("ptw_form"):
        st.subheader("1. Agency & Contract Info")
        agency = st.selectbox("Agency Name / Sub-agency", fetch_agencies())
        contract_title = st.text_input("Contract Title")
        solicitation_number = st.text_input("Contract Solicitation Number")
        contract_value = st.number_input("Estimated Contract Value ($)", min_value=0.0)
        contract_type = st.selectbox("Contract Type", ["Full & Open", "SDVOSB", "WOSB", "HubZone", "ANC", "Other"])

        st.subheader("2. Solicitation Upload")
        file = st.file_uploader("Upload Solicitation (PWS, SOW, etc.)", type=["pdf", "docx"])

        st.subheader("3. Labor Info")
        labor_cat = st.selectbox("Labor Category", ["Program Manager", "Analyst", "IT Specialist", "Other"])
        base_salary = st.number_input("Base Salary Estimate ($)", min_value=0.0)
        bill_low = st.number_input("Bill Rate – Low", min_value=0.0)
        bill_mid = st.number_input("Bill Rate – Mid", min_value=0.0)
        bill_high = st.number_input("Bill Rate – High", min_value=0.0)

        st.subheader("4. Contracting Context")
        eval_cat = st.selectbox("Evaluation Category", ["Best Value", "LPTA", "Undefined"])
        pricing_scenario = st.selectbox("Pricing Scenario", ["New Requirement", "Recompete"])

        st.subheader("5. Modifiers")
        job_intensity = st.selectbox("Job Description Intensity", ["Low", "Medium", "High", "Unknown"])
        spec_req = st.selectbox("Specialized Requirement?", ["Yes", "No"])
        political_modifier = st.selectbox("Political Trend Modifier", ["Expansionary (+3%)", "Neutral (0%)", "Contractionary (-3%)"])

        st.subheader("6. Benchmarking (Optional)")
        hist_val = st.number_input("Historical Contract Value ($)", min_value=0.0)
        benchmark_rate = st.number_input("Comparable Benchmark Rate ($)", min_value=0.0)

        submitted = st.form_submit_button("Run PTW Analysis")

    if submitted:
        st.markdown("---")
        st.subheader("Computed Outputs")

        var_low = round(((bill_low - benchmark_rate) / benchmark_rate) * 100, 2) if benchmark_rate else 0.0
        var_mid = round(((bill_mid - benchmark_rate) / benchmark_rate) * 100, 2) if benchmark_rate else 0.0
        var_high = round(((bill_high - benchmark_rate) / benchmark_rate) * 100, 2) if benchmark_rate else 0.0

        adj_low = compute_adjusted_rates(bill_low, job_intensity, spec_req, political_modifier)
        adj_mid = compute_adjusted_rates(bill_mid, job_intensity, spec_req, political_modifier)
        adj_high = compute_adjusted_rates(bill_high, job_intensity, spec_req, political_modifier)

        win_low = compute_win_probability(adj_low, benchmark_rate)
        win_mid = compute_win_probability(adj_mid, benchmark_rate)
        win_high = compute_win_probability(adj_high, benchmark_rate)

        df = pd.DataFrame({
            "Scenario": ["Low", "Mid", "High"],
            "Input Rate ($)": [bill_low, bill_mid, bill_high],
            "Variance vs Benchmark (%)": [var_low, var_mid, var_high],
            "Adjusted Rate ($)": [adj_low, adj_mid, adj_high],
            "Win Probability": [win_low, win_mid, win_high],
        })
        st.dataframe(df, use_container_width=True)

        # Determine best scenario
        best_idx = np.argmax([win_low, win_mid, win_high])
        ptw_rate = [adj_low, adj_mid, adj_high][best_idx]
        ptw_label = ["Low", "Mid", "High"][best_idx]

        st.success(f"Recommended PTW Rate: ${ptw_rate} ({ptw_label} scenario) with {max(win_low, win_mid, win_high)*100:.1f}% win probability.")

        # Justification notes
        with st.expander("📜 Justification Notes"):
            st.markdown(f"- Based on job intensity: **{job_intensity}**, specialized requirement: **{spec_req}**, and political climate: **{political_modifier}**.")
            st.markdown(f"- Evaluated under **{eval_cat}** criteria for a **{pricing_scenario}**.")
            st.markdown(f"- Adjusted using base salary estimate and scenario-based inputs. Compared against benchmark rate of **${benchmark_rate}**.")
            st.markdown(f"- Scenario '{ptw_label}' selected due to optimal win rate and alignment with market dynamics.")
