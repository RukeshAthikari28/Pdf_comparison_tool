# 📄 PDF Comparison Tool

A Streamlit-based web application that allows users to upload and compare two PDF documents. The differences between the documents are highlighted in color:  
🟢 **Added content** – Green  
🔴 **Removed content** – Red  
🟡 **Modified content** – Yellow

---

## 🚀 Features

- Upload two PDF documents
- Extract and compare text content
- Visualize differences with color-coded highlights
- Generate a summary report of:
  - Number of additions
  - Number of deletions
  - Number of modifications
- Clean and user-friendly Streamlit interface

---

## 🛠️ Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/)
- **Text Extraction**: PyMuPDF (fitz)
- **Text Comparison**: Python’s `difflib`
- **OCR Support** *(Future Scope)*: `pytesseract`, `pdfplumber`

---

