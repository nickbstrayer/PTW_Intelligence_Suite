import spacy
import streamlit as st
from PyPDF2 import PdfReader
import os

@st.cache_resource
def load_model():
    try:
        # Try loading the model directly
        return spacy.load("en_core_web_sm")
    except OSError:
        # Automatically download if not available
        from spacy.cli import download
        download("en_core_web_sm")
        return spacy.load("en_core_web_sm")

def extract_text_from_pdf(uploaded_file):
    reader = PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

def classify_text(text, nlp):
    doc = nlp(text)
    # Example logic: count token length or keyword matches to assign "intensity"
    token_count = len(doc)
    if token_count > 1200:
        intensity = "High"
    elif token_count > 600:
        intensity = "Medium"
    else:
        intensity = "Low"

    # Dummy uniqueness measure: count distinct nouns
    nouns = [token.text.lower() for token in doc if token.pos_ == "NOUN"]
    unique_nouns = len(set(nouns))

    return {
        "intensity": intensity,
        "unique_noun_count": unique_nouns,
        "token_count": token_count
    }
