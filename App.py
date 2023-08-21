import streamlit as st
import openai
from PyPDF2 import PdfFileReader
from docx import Document

# Set your OpenAI API key here
openai.api_key = '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'


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

uploaded_file = st.file_uploader("Upload a file", type=["pdf", "docx"])

if uploaded_file is not None:
    file_extension = uploaded_file.name.split('.')[-1].lower()
    if file_extension == 'pdf':
        doc_text = extract_text_from_pdf(uploaded_file)
    elif file_extension == 'docx':
        doc_text = extract_text_from_docx(uploaded_file)
    else:
        st.write("Unsupported file format")
        st.stop()

    st.text("Document text:")
    st.write(doc_text)

    question = st.text_input("Ask a question:")

    if st.button("Get Answer"):
        prompt = f"Document: {doc_text}\nQuestion: {question}\nAnswer:"
        response = openai.Completion.create(
            engine="davinci-codex",  # Use the codex engine for code-related tasks
            prompt=prompt,
            max_tokens=100
        )
        answer = response.choices[0].text.strip()

        st.write("Generated Answer:")
        st.write(answer)
