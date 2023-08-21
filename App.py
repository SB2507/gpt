import streamlit as st
import requests
import pdfplumber
from transformers import AutoTokenizer, AutoModelForCausalLM
from docx import Document
from PyPDF2 import PdfFileReade

# Set your OpenAI API key here
openai.api_key = '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'

# Load GPT-3 model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-neo-2.7B")
model = AutoModelForCausalLM.from_pretrained("EleutherAI/gpt-neo-2.7B")

def fetch_text_from_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None

def extract_text_from_pdf(pdf_file):
    pdf_text = ""
    pdf_reader = PdfFileReader(pdf_file)
    for page_num in range(pdf_reader.numPages):
        page = pdf_reader.getPage(page_num)
        pdf_text += page.extractText()
    return pdf_text

def extract_text_from_docx(docx_file):
    doc = Document(docx_file)
    docx_text = "\n".join(para.text for para in doc.paragraphs)
    return docx_text

st.title("Document AI Assistant")

source_option = st.radio("Select Source:", ("URL", "Upload PDF", "Upload Word"))

if source_option == "URL":
    url = st.text_input("Enter the URL of the document:")
    if url:
        doc_text = fetch_text_from_url(url)
else:
    uploaded_file = st.file_uploader("Upload a file", type=["pdf", "docx"])

    if source_option == "Upload PDF" and uploaded_file is not None:
        doc_text = extract_text_from_pdf(uploaded_file)
    elif source_option == "Upload Word" and uploaded_file is not None:
        doc_text = extract_text_from_docx(uploaded_file)

if "doc_text" in locals():
    st.text("Document text:")
    st.write(doc_text)

    question = st.text_input("Ask a question:")

    if st.button("Get Answer"):
        prompt = f"Document text: {doc_text}\nQuestion: {question}\nAnswer:"

        response = openai.Completion.create(
            engine="text-davinci-003",  # Use the Davinci engine for text completion
            prompt=prompt,
            max_tokens=100
        )
        answer = response.choices[0].text.strip()

        st.write("Generated Answer (using OpenAI GPT-3):")
        st.write(answer)
