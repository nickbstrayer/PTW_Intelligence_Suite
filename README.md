# PTW Intelligence Suite

A unified Streamlit-based platform for federal pricing analysis, AI-based job classification, salary prediction, and PTW simulation.

## Features
- 🔐 Secure Login with Streamlit Session State
- 🧮 Price-to-Win Calculator (with competitors, visual charts, export)
- 📥 Salary Estimator powered by AI
- 🤖 Resume/SOW Classifier for Job Intensity & Specialization
- 📊 Dashboard for Competitive Rate Analysis

## Getting Started

1. Clone this repository
2. Ensure Python 3.8+ is installed
3. Create a virtual environment and install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   streamlit run ptw_main_launcher.py
   ```

## Project Structure

- `ptw_main_launcher.py` – main launcher and navigation
- `/pages/` – feature modules
- `/scripts/` – authentication logic
- `/models/` – AI/ML models (e.g., salary estimator)

---
Developed by Nick B · 2025
