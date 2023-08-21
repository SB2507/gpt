# app.py
import streamlit as st
from PIL import Image
import pytesseract
import os
import io
import openai
import PyPDF2
import python_pptx
import docx

# Set your OpenAI API key here
openai.api_key = 'YOUR_OPENAI_API_KEY'

st.title("AI Document Assistant")

uploaded_file = st.file_uploader("Upload a file", type=["pdf", "pptx", "docx", "png", "jpg", "jpeg"])

if uploaded_file is not None:
    file_extension = os.path.splitext(uploaded_file.name)[1].lower()

    if file_extension == '.pdf':
        # Process PDF using PyPDF2
        pdf_data = uploaded_file.read()
        pdf_text = ""
        with io.BytesIO(pdf_data) as pdf_io:
            pdf_reader = PyPDF2.PdfReader(pdf_io)
            for page in pdf_reader.pages:
                pdf_text += page.extract_text()

        text = pdf_text

    elif file_extension == '.pptx':
        # Process PowerPoint using python-pptx
        ppt_data = uploaded_file.read()
        ppt_text = ""
        with io.BytesIO(ppt_data) as ppt_io:
            ppt = python_pptx.Presentation(ppt_io)
            for slide in ppt.slides:
                for shape in slide.shapes:
                    if shape.has_text_frame:
                        ppt_text += shape.text

        text = ppt_text

    elif file_extension == '.docx':
        # Process Word document using docx
        docx_data = uploaded_file.read()
        docx_text = ""
        with io.BytesIO(docx_data) as docx_io:
            doc = docx.Document(docx_io)
            for para in doc.paragraphs:
                docx_text += para.text

        text = docx_text

    elif file_extension in ['.png', '.jpg', '.jpeg']:
        # Process image using pytesseract
        img = Image.open(uploaded_file)
        img_text = pytesseract.image_to_string(img)
        text = img_text

    st.text("Document text:")
    st.write(text)  # Display extracted text

    # User input for the question
    question = st.text_input("Ask a question:")

    if st.button("Get Answer"):
        # Construct the prompt for the ChatGPT API
        prompt = f"Document text: {text}\nQuestion: {question}\nAnswer:"

        # Generate a response using the ChatGPT API
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=100
        )
        answer = response.choices[0].text.strip()

        # Display the generated answer
        st.write("Generated Answer:")
        st.write(answer)
