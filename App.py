import streamlit as st
import PyPDF2

def pdf_to_text(pdf_file):
    text = ""
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def main():
    st.set_page_config(page_title="PDF to Text Converter")
    st.title("PDF to Text Converter")

    pdf_file = st.file_uploader("Upload a PDF file", type=["pdf"])

    if pdf_file is not None:
        if st.button("Convert to Text"):
            extracted_text = pdf_to_text(pdf_file)
            st.subheader("Extracted Text:")
            st.write(extracted_text)

if __name__ == "__main__":
    main()
