import streamlit as st
import PyPDF2
import openai


# Replace "YOUR_OPENAI_API_KEY" with your actual OpenAI API key
openai.api_key = "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"

import streamlit as st
import PyPDF2

def pdf_to_text(pdf_path):
    with open(pdf_path, "rb") as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page_num in range(len(pdf_reader.pages)):
            text += pdf_reader.pages[page_num].extract_text()
    return text

def main():
    st.title("PDF to Text Converter")

    pdf_path = st.file_uploader("Upload PDF File", type=["pdf"])

    if pdf_path:
        st.write("PDF uploaded successfully.")
        pdf_text = pdf_to_text(pdf_path)
        st.subheader("Extracted Text:")
        st.text(pdf_text)

if __name__ == "__main__":
    main()
