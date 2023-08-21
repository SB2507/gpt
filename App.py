import streamlit as st
import fitz  # PyMuPDF
import openai

openai.api_key = "YOUR_OPENAI_API_KEY"

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text("text")
    return text

def chat_with_bot(user_input):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user_input,
        max_tokens=50
    )
    return response.choices[0].text.strip()

def main():
    st.title("PDF Chatbot")

    pdf_path = st.file_uploader("Upload PDF File", type=["pdf"])

    if pdf_path:
        st.write("PDF uploaded successfully.")
        user_input = st.text_input("Ask a question or provide a prompt:")
        if st.button("Chat with Bot"):
            pdf_text = extract_text_from_pdf(pdf_path)
            full_input = f"PDF Content: {pdf_text}\nUser Input: {user_input}\nBot:"
            bot_response = chat_with_bot(full_input)
            st.write("Bot Response:", bot_response)

if __name__ == "__main__":
    main()
