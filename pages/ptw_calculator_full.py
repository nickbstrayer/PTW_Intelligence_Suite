import streamlit as st
import numpy as np

def render_ptw_calculator():
    st.markdown("""
        <h2 style='margin-bottom: 1rem;'>📊 PTW Calculator – Full</h2>
        <p>This advanced form integrates agency metadata, pricing strategy, labor category modeling, economic modifiers, benchmarking, and AI-enhanced win probabilities to produce an optimized Price-to-Win recommendation.</p>
    """, unsafe_allow_html=True)

    st.subheader("Agency & Contract Info")
    agency_name = st.text_input("Agency Name or Sub-agency")
    contract_title = st.text_input("Contract Title")
    solicitation_number = st.text_input("Solicitation Number")
    contract_value = st.number_input("Estimated Contract Value ($)", step=10000.0)
    contract_type = st.selectbox("Contract Type", ["Full & Open", "SDVOSB", "WOSB", "HubZone", "ANC", "Other"])

    st.subheader("Labor & Rate Inputs")
    labor_category = st.selectbox("Labor Category", ["Program Manager", "Analyst", "Engineer", "Technician"])
    base_salary = st.number_input("Base Salary Estimate ($)", step=1000.0)
    rate_low = st.number_input("Bill Rate – Low ($)", step=1.0)
    rate_mid = st.number_input("Bill Rate – Mid ($)", step=1.0)
    rate_high = st.number_input("Bill Rate – High ($)", step=1.0)

    st.subheader("Contracting Context")
    evaluation_category = st.selectbox("Evaluation Category", ["Best Value", "LPTA", "Undefined"])
    pricing_scenario = st.selectbox("Pricing Scenario", ["New Requirement", "Recompete"])

    st.subheader("Performance Modifiers")
    intensity = st.selectbox("Job Description Intensity", ["Low", "Medium", "High", "Unknown"])
    specialized = st.selectbox("Specialized Requirement?", ["Yes", "No"])
    trend_modifier = st.selectbox("Political Trend Modifier", ["Expansionary (+3%)", "Neutral (0%)", "Contractionary (-3%)"])

    st.subheader("Benchmarking & Reference Data")
    hist_contract = st.number_input("Historical Award Value ($)", step=1000.0)
    benchmark_rate = st.number_input("Comparable GSA Benchmark Rate ($)", step=1.0)

    if benchmark_rate > 0:
        variance_low = (rate_low - benchmark_rate) / benchmark_rate
        variance_mid = (rate_mid - benchmark_rate) / benchmark_rate
        variance_high = (rate_high - benchmark_rate) / benchmark_rate
    else:
        variance_low = variance_mid = variance_high = 0.0

    # Adjusted Rates Based on Modifiers
    def apply_modifiers(rate, intensity, specialized, trend):
        adjustment = 1.0
        if intensity == "High":
            adjustment += 0.07
        elif intensity == "Medium":
            adjustment += 0.04
        elif intensity == "Low":
            adjustment += 0.01

        if specialized == "Yes":
            adjustment += 0.03

        if trend == "Expansionary (+3%)":
            adjustment += 0.03
        elif trend == "Contractionary (-3%)":
            adjustment -= 0.03

        return rate * adjustment

    adj_low = apply_modifiers(rate_low, intensity, specialized, trend_modifier)
    adj_mid = apply_modifiers(rate_mid, intensity, specialized, trend_modifier)
    adj_high = apply_modifiers(rate_high, intensity, specialized, trend_modifier)

    # Win Probability (mock regression style logic)
    def win_probability(rate, benchmark):
        if benchmark <= 0:
            return 0.50
        diff = abs(rate - benchmark)
        if diff < 5:
            return 0.8
        elif diff < 10:
            return 0.6
        elif diff < 15:
            return 0.4
        else:
            return 0.2

    win_low = win_probability(adj_low, benchmark_rate)
    win_mid = win_probability(adj_mid, benchmark_rate)
    win_high = win_probability(adj_high, benchmark_rate)

    # Recommendation
    rates = [adj_low, adj_mid, adj_high]
    wins = [win_low, win_mid, win_high]
    recommended_index = int(np.argmax(wins))
    recommended_rate = rates[recommended_index]
    justification = ["Low scenario offers best value.", "Mid-range optimizes value and win rate.", "High value justified by technical superiority."][recommended_index]

    st.subheader("📈 Price-to-Win Output")
    st.write("**Adjusted Rates:**")
    st.text(f"Low: ${adj_low:,.2f} | Mid: ${adj_mid:,.2f} | High: ${adj_high:,.2f}")
    st.write("**Win Probabilities:**")
    st.text(f"Low: {win_low*100:.1f}% | Mid: {win_mid*100:.1f}% | High: {win_high*100:.1f}%")
    st.success(f"✅ Recommended PTW Rate: **${recommended_rate:,.2f}**")
    st.caption(f"Justification: {justification}")
