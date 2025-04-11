# Pdf_comparison_tool 
A Streamlit app to compare two PDFs and highlight the differences.

## Features
- Upload two PDF files
- Extract text content
- Highlight added (green), removed (red), and modified (yellow) text
- Summary report of changes
- Clean UI with Streamlit

## Installation

```bash
git clone https://github.com/yourname/pdf-comparator.git
cd pdf-comparator
pip install -r requirements.txt
```

## Run the App
```bash
streamlit run app.py
```

## Folder Structure
- `app.py`: Main Streamlit app
- `utils/`: Utility modules for PDF handling and comparison

## Future Improvements
- OCR for scanned PDFs
- Use LLM to summarize content change
- Handle large files efficiently