import streamlit as st
import spacy
from PyPDF2 import PdfReader

@st.cache_resource
def load_model():
    return spacy.load("en_core_web_sm")

def extract_text(uploaded_file):
    reader = PdfReader(uploaded_file)
    return "".join(page.extract_text() or "" for page in reader.pages)

def classify_text(text):
    intensity_keywords = ["lead", "manage", "coordinate", "complex", "strategic"]
    unique_keywords = ["clearance", "cyber", "deployment", "language", "clinical"]

    intensity_score = sum(word in text.lower() for word in intensity_keywords)
    unique_score = sum(word in text.lower() for word in unique_keywords)

    intensity = "High" if intensity_score >= 4 else "Medium" if intensity_score >= 2 else "Low"
    unique = "Yes" if unique_score >= 1 else "No"

    return intensity, unique

def render():
    st.header("🤖 AI Job Classifier")
    st.write("Upload a job description or resume to predict job intensity and uniqueness.")

    uploaded = st.file_uploader("Upload PDF file", type="pdf")
    if uploaded:
        nlp = load_model()
        text = extract_text(uploaded)
        intensity, unique = classify_text(text)
        st.success(f"Job Intensity: {intensity} | Specialized Requirement: {unique}")
        with st.expander("Show Extracted Text"):
            st.text(text[:2000])
