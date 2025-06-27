import streamlit as st
import requests
import json
import time

# Streamlit page setup
st.set_page_config(page_title="🤖 LLaMA Meena Mahanth's AI Chatbot", layout="centered")
st.title("🤖 Chat with LLaMA 3.2:1B")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {"role": "🧠", "content": "I am an AI assistant 🤖 developed by Madireddy Meena Mahanth Harinadh 👨‍💻"}
    ]

# Function to stream response from Ollama
def stream_response_from_ollama(messages, model="llama3.2:1b"):
    url = "http://localhost:11434/api/chat"
    response = requests.post(url, json={"model": model, "messages": messages}, stream=True)

    for line in response.iter_lines():
        if line:
            try:
                data = line.decode("utf-8")
                json_data = json.loads(data)
                if "message" in json_data and "content" in json_data["message"]:
                    yield json_data["message"]["content"]
            except json.JSONDecodeError:
                continue

# Display chat history
for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input box for new user message
user_input = st.chat_input("Say 'Hi' 👋 To Meena Mahanth's Chatbot")

if user_input:
    # Add user message
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Stream and display LLaMA response
    with st.chat_message("assistant"):
        with st.spinner("🤔 LLaMA Thinking...💭"):
            placeholder = st.empty()
            full_response = ""
            for chunk in stream_response_from_ollama(st.session_state.chat_history):
                full_response += chunk
                placeholder.markdown(full_response + "▌")  # Typing effect cursor
                time.sleep(0.02)  # Speed control

            placeholder.markdown(full_response)  # Final render

    # Save assistant message to history
    st.session_state.chat_history.append({"role": "assistant", "content": full_response})
