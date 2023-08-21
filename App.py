# app.py
import streamlit as st
from PIL import Image
import pytesseract
import os
import io
import openai
import PyPDF2
#import python_pptx
import docx

# Set your OpenAI API key here
openai.api_key = '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'

st.title("AI Document Assistant")

uploaded_file = st.file_uploader("Upload a file", type=["pdf", "pptx", "docx", "png", "jpg", "jpeg"])

# ... rest of the code ...

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
