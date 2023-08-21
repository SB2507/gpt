import streamlit as st
import pdfplumber
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

# Load pre-trained model and tokenizer
model_name = "gpt2-medium"  # You can choose other models too
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)
model.eval()

# Function to generate a response
def generate_response(input_text, max_length=50):
    input_ids = tokenizer.encode(input_text, return_tensors="pt")
    with torch.no_grad():
        output = model.generate(input_ids, max_length=max_length, num_return_sequences=1)
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return response

# Function to extract text from a PDF
def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    return text

# Streamlit app
def main():
    st.title("Chatbot Learning from PDFs")
    
    uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])
    if uploaded_file is not None:
        st.write("PDF Uploaded Successfully!")

        text = extract_text_from_pdf(uploaded_file)
        st.write("Extracted Text:")
        st.text_area("PDF Text", text)

        user_input = st.text_input("You:")
        if st.button("Send"):
            response = generate_response(user_input)
            st.write("Chatbot:", response)

if __name__ == "__main__":
    main()
