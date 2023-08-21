import streamlit as st
import PyPDF2
import openai


# Replace "YOUR_OPENAI_API_KEY" with your actual OpenAI API key
openai.api_key = "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"

def extract_text_from_pdf(uploaded_pdf):
    pdf_text = ""
    pdf_file = uploaded_pdf.read()  # Read the uploaded PDF content as bytes
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    for page_num in range(len(pdf_reader.pages)):
        pdf_text += pdf_reader.pages[page_num].extract_text()
    return pdf_text

def chat_with_bot(pdf_text, user_input):
    full_input = f"PDF Content: {pdf_text}\nUser Input: {user_input}\nBot:"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=full_input,
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
            bot_response = chat_with_bot(pdf_text, user_input)
            st.write("Bot Response:", bot_response)

if __name__ == "__main__":
    main()

