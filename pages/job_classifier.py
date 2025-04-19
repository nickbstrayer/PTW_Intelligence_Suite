import streamlit as st

try:
    import spacy
    nlp = spacy.load("en_core_web_sm")  # Make sure this model is added in requirements.txt
except Exception as e:
    st.error(f"Failed to load spaCy model: {e}")
    nlp = None

def render_job_classifier():
    st.title("🤖 AI Job Classifier")

    st.markdown("Paste a job description below to classify it using AI NLP:")
    job_text = st.text_area("Job Description")

    if st.button("🔍 Classify Job"):
        if not nlp:
            st.error("spaCy model is not loaded. Please check setup.")
            return

        doc = nlp(job_text)
        ents = [(ent.text, ent.label_) for ent in doc.ents]

        if ents:
            st.markdown("### 🔍 Extracted Entities:")
            for text, label in ents:
                st.markdown(f"- **{label}**: {text}")
        else:
            st.info("No recognizable entities found.")

