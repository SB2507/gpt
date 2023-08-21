
# Replace "YOUR_OPENAI_API_KEY" with your actual OpenAI API key
openai.api_key = "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"

import streamlit as st
from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def main():
    st.title("PDF Text Extraction")

    pdf_path = st.file_uploader("Upload PDF File", type=["pdf"])

    if pdf_path:
        st.write("PDF uploaded successfully.")
        pdf_text = extract_text_from_pdf(pdf_path)
        st.subheader("Extracted Text:")
        st.text(pdf_text)

if __name__ == "__main__":
    main()

