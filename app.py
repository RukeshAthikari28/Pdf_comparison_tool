# app.py
import os
import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
import difflib
import tempfile
import faiss
from langchain.embeddings import GooglePalmEmbeddings

# Load environment variables
load_dotenv()

# Get Google API key from .env
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Set page config
st.set_page_config(page_title="PDF Comparison Tool", layout="wide")
st.title("PDF Comparison Tool")

# Helper to extract text from PDF
def extract_text_from_pdf(pdf_file):
    reader = PdfReader(pdf_file)
    text = "\n".join(page.extract_text() or "" for page in reader.pages)
    return text

# Helper to compare two texts and return difference summary
def compare_texts(text1, text2):
    d = difflib.Differ()
    diff = list(d.compare(text1.splitlines(), text2.splitlines()))

    added, removed, modified = 0, 0, 0
    result = []

    for line in diff:
        if line.startswith("+ "):
            added += 1
            result.append(f"<span style='background-color:#e6f4ea;color:#0f5132;'>{line[2:]}</span>")
        elif line.startswith("- "):
            removed += 1
            result.append(f"<span style='background-color:#f8d7da;color:#842029;'>{line[2:]}</span>")
        elif line.startswith("? "):
            modified += 1
            result.append(f"<span style='background-color:#fff3cd;color:#664d03;'>{line[2:]}</span>")
        else:
            result.append(line[2:])

    html_output = "<br>".join(result)
    return html_output, added, removed, modified

# Upload PDFs
col1, col2 = st.columns(2)
with col1:
    pdf1 = st.file_uploader("Upload First PDF", type="pdf")
with col2:
    pdf2 = st.file_uploader("Upload Second PDF", type="pdf")

if pdf1 and pdf2:
    text1 = extract_text_from_pdf(pdf1)
    text2 = extract_text_from_pdf(pdf2)

    with st.spinner("Comparing PDFs..."):
        diff_html, added, removed, modified = compare_texts(text1, text2)

    st.markdown("### Differences")
    st.markdown(diff_html, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### Summary Report")
    st.write(f" Added Lines: {added}")
    st.write(f" Removed Lines: {removed}")
    st.write(f" Modified Lines: {modified}")

else:
    st.info("Please upload two PDFs to compare.")

# Optional placeholder to use FAISS and embeddings
# This is where you can further integrate vector-based search if needed
if GOOGLE_API_KEY:
    st.markdown("<small>Google API key detected. FAISS and embeddings setup ready.</small>", unsafe_allow_html=True)
    # Example: Load embeddings using GooglePalmEmbeddings (requires LangChain integration)
    # embeddings = GooglePalmEmbeddings(google_api_key=GOOGLE_API_KEY)
    # Use embeddings with FAISS for similarity search, document QA, etc.
else:
    st.warning("Google API key not found in .env file.")
