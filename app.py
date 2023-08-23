import streamlit as st
import pytesseract
from PIL import Image
import fitz  # PyMuPDF
import tempfile
import os

# Set the title of the Streamlit app
st.title("Text Extraction App")

def ocr_text(text):
    try:
        extracted_text = text
        return extracted_text
    except Exception as e:
        return str(e)

# Streamlit UI components
st.sidebar.header("Options")
file_type = st.sidebar.selectbox("Select File Type", ["PDF"])
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])
    if uploaded_file is not None:
        if st.button("Extract and Perform OCR"):
            # Convert PDF to text using PyMuPDF
            with tempfile.NamedTemporaryFile(delete=False) as temp_pdf:
                temp_pdf.write(uploaded_file.read())
                temp_pdf_path = temp_pdf.name
            
            pdf_document = fitz.open(temp_pdf_path)
            num_pages = pdf_document.page_count
            extracted_text = ""
            for page_num in range(num_pages):
                page = pdf_document[page_num]
                extracted_text += page.get_text()
            pdf_document.close()

            # Perform OCR on extracted text
            extracted_text = ocr_text(extracted_text)
            
            st.subheader("Extracted Text:")
            st.write(extracted_text)
            
            # Clean up the temporary PDF file
            os.remove(temp_pdf_path)
