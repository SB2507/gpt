import streamlit as st
import fitz  # PyMuPDF

def pdf_to_text(pdf_file):
    text = ""
    pdf_document = fitz.open(stream=pdf_file.read(), filetype="pdf")
    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        text += page.get_text("text")
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
