import streamlit as st
import pytesseract
from PIL import Image
import fitz  # PyMuPDF

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

if file_type == "PDF":
    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])
    if uploaded_file is not None:
        if st.button("Extract and Perform OCR"):
            # Convert PDF to text using PyMuPDF
            pdf_document = fitz.open(uploaded_file)
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
