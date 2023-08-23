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

if file_type == "PDF":
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
            # Extracted text is set to sample text for testing purposes
            extracted_text = ocr_text("This is a sample extracted text.")
            
            st.subheader("Extracted Text:")
            st.write(extracted_text)
            
            # Provide a download button for the extracted text
            with st.expander("Download Extracted Text"):
                st.download_button(
                    label="Download Text",
                    data=extracted_text.encode("utf-8"),
                    file_name="extracted_text.txt",
                    mime="text/plain"
                )
            
            # Clean up the temporary PDF file
            os.remove(temp_pdf_path)
