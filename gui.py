import streamlit as st
import random
import time

st.title("Simple Chat")

# Initialize chat history if not already initialized
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
prompt = st.chat_input("What is up?")
if prompt:
    # Display user message and add to chat history
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Generate bot response
    def response_generator():
        responses = [
            "Hello there! How can I assist you today?",
            "Hi, human! Is there anything I can help you with?",
            "Do you need help?",
        ]
        selected_response = random.choice(responses)
        time.sleep(len(selected_response) * 0.05)  # Simulate typing delay
        return selected_response

    # Display bot response after delay
    bot_response = response_generator()
    with st.chat_message("assistant"):
        st.markdown(bot_response)
    st.session_state.messages.append({"role": "assistant", "content": bot_response})
