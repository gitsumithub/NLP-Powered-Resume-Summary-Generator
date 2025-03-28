import streamlit as st
from summarizer import summarize_resume
import PyPDF2
import io

st.set_page_config(page_title="Resume Summarizer", layout="centered")

st.title("NLP-Powered Resume Summarizer")

uploaded_file = st.file_uploader("Upload a resume (PDF format)", type=["pdf"])

if uploaded_file:
    reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()

    st.subheader("Extracted Text")
    st.write(text[:1000] + "...")  # Preview first 1000 chars

    if st.button("Summarize Resume"):
        with st.spinner("Generating summary..."):
            summary = summarize_resume(text)
            st.subheader("Generated Summary")
            st.success(summary)
