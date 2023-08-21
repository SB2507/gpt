import streamlit as st
import openai

# Set your OpenAI API key here
openai.api_key = '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'
def chat_with_bot(prompt):
    response = openai.Completion.create(
        engine="davinci",  # Use the 'davinci' engine for the best performance
        prompt=prompt,
        max_tokens=50  # Limit the response length
    )
    return response.choices[0].text.strip()

def main():
    st.title("Chatbot with Streamlit")
    st.write("Chat with the bot:")
    
    user_input = st.text_input("You:")
    
    if user_input:
        if user_input.lower() == "exit":
            st.write("Chatbot: Goodbye!")
        else:
            prompt = f"You: {user_input}\nChatbot:"
            response = chat_with_bot(prompt)
            st.write("Chatbot:", response)

if __name__ == "__main__":
    main()
