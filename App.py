 
import streamlit as st
import openai

# Set your OpenAI API key here
openai.api_key = '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'

# Extract text from a PDF in chunks
def extract_text_in_chunks(pdf_path, chunk_size=10000):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
            if len(text) >= chunk_size:
                yield text
                text = ""
        if text:
            yield text

# Generate a response using GPT-3
def generate_gpt3_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=50  # Adjust as needed
    )
    return response.choices[0].text.strip()

# Main Streamlit app
def main():
    st.title("PDF Chatbot with GPT-3")

    pdf_path = 'path_to_your_pdf.pdf'
    text_chunks = extract_text_in_chunks(pdf_path)

    st.write("Ask a question:")
    user_question = st.text_input("")

    if st.button("Ask"):
        if user_question:
            answer = search_for_answer(text_chunks, user_question)
            st.write("Keyword-based Answer:", answer)

            gpt3_prompt = f"Q: {user_question}\nA: {answer}\nQ:"
            gpt3_response = generate_gpt3_response(gpt3_prompt)
            st.write("GPT-3 Response:", gpt3_response)

if __name__ == "__main__":
    main()
