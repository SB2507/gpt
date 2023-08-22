import streamlit as st
import fitz  # PyMuPDF for PDF processing
import faiss  # FAISS for vector similarity search
import openai  # OpenAI for embeddings
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Main function
def main():
    # Set Streamlit page configuration
    st.set_page_config(page_title="Chat PDF")
    st.header("Chat PDF 💬")
    
    # Upload PDF file
    pdf = st.file_uploader("Upload your PDF file", type="pdf")
    
    # Initialize OpenAI API
    openai.api_key =("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")
    
    # Initialize FAISS index
    index = faiss.IndexFlatL2(768)  # Assuming 768-dimensional embeddings
    
    # If a PDF is uploaded
    if pdf is not None:
        # Extract text from PDF pages
        pdf_document = fitz.open(pdf)
        text = ""
        for page_num in range(pdf_document.page_count):
            page = pdf_document.load_page(page_num)
            text += page.get_text("text")
        
        # Split text into chunks
        chunk_size = 1000
        text_chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
        
        # Create embeddings for text chunks
        embeddings = []
        for chunk in text_chunks:
            response = openai.Embedding.create(texts=[chunk])
            embeddings.append(response['data'][0]['vector'])
        embeddings = faiss.normalize_L2(embeddings)
        
        # Add embeddings to FAISS index
        index.add(embeddings)
        
        # Get user input question
        query = st.text_input("Type your question:")
        if query:
            # Embed the query
            query_embedding = openai.Embedding.create(texts=[query])['data'][0]['vector']
            query_embedding = faiss.normalize_L2(query_embedding)
            
            # Perform similarity search
            num_results = 5
            distances, indices = index.search(query_embedding, num_results)
            
            # Display search results
            for i in range(num_results):
                st.write(f"Result {i+1}: Similarity Score {1 - distances[0][i]:.2f}")
                st.write(text_chunks[indices[0][i]])
                st.write("-" * 30)

# Run the main function when the script is executed
if __name__ == '__main__':
    main()
