import streamlit as st
import requests
from transformers import AutoTokenizer, AutoModelForCausalLM
 
from PyPDF2 import PdfFileReader

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

 
# Custom CSS styling
st.markdown(
    """
    <style>
    .chat-container {
        max-width: 800px;
        margin: 0 auto;
        padding: 20px;
        background-color: #f4f4f4;
        border-radius: 20px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }
    .message {
        padding: 10px;
        margin: 10px 0;
        border-radius: 10px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        max-width: 80%;
    }
    .user-message {
        text-align: right;
        background-color: #DCF8C6;
        align-self: flex-end;
    }
    .assistant-message {
        text-align: left;
        background-color: #E0E0E0;
        align-self: flex-start;
    }
    .chat-input {
        width: 100%;
        padding: 10px;
        border: none;
        border-radius: 20px;
        background-color: #fff;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    }
    .chat-button {
        background-color: #007BFF;
        color: #fff;
        padding: 10px 20px;
        border: none;
        border-radius: 20px;
        cursor: pointer;
        transition: background-color 0.3s;
    }
    .chat-button:hover {
        background-color: #0056b3;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("WhatsApp-like Document AI Assistant")

# Sidebar for source selection
source_option = st.sidebar.radio("Select Source:", ("URL", "Upload PDF", "Upload Word"))

# Display WhatsApp-like chat interface
with st.sidebar:
    st.image("https://image.freepik.com/free-vector/whatsapp-icon_1057-2466.jpg", width=50)
st.sidebar.title("Chat")

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
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)

    st.markdown('<div class="message user-message">', unsafe_allow_html=True)
    st.text_area("User", key="user_message", class_="chat-input")
    st.markdown('</div>', unsafe_allow_html=True)

    question = st.text_input("Ask a question:", class_="chat-input")

    if st.button("Get Answer", class_="chat-button"):
        prompt = f"Document text: {doc_text}\nQuestion: {question}\nAnswer:"

        response = openai.Completion.create(
            engine="text-davinci-003",  # Use the Davinci engine for text completion
            prompt=prompt,
            max_tokens=100
        )
        answer = response.choices[0].text.strip()

        st.markdown('<div class="message assistant-message">', unsafe_allow_html=True)
        st.write(answer)
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
