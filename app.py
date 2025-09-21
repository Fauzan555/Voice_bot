# Save this as app.py
import streamlit as st
from streamlit_chat import message
import pyttsx3

st.set_page_config(page_title="Voice Chatbot Demo", page_icon="🤖")

st.title("Voice Chatbot Demo")
st.write("Click the button and speak your question. The bot will respond in text and voice.")

# Initialize pyttsx3 text-to-speech engine
engine = pyttsx3.init()

# Predefined answers
predefined_answers = {
    "life story": "I’m an AI model designed to assist and provide information. I learn continuously and love helping people solve problems in creative ways.",
    "superpower": "Understanding and generating human-like text to make communication seamless and insightful.",
    "top 3 areas": "I aim to improve real-time reasoning, creative problem-solving, and understanding complex emotions in human conversation.",
    "misconceptions": "People sometimes think I have personal experiences or feelings, but I generate responses based on patterns in data.",
    "boundaries": "I experiment with new types of questions and domains to improve my accuracy and usefulness continuously."
}

# Chat history
if 'history' not in st.session_state:
    st.session_state.history = []

# Text input for simulation (since browser voice input is tricky in Streamlit)
user_input = st.text_input("Type or paste your question here:")

if st.button("Send"):
    text = user_input.lower()
    reply = "Sorry, I didn't understand. Please ask one of the sample questions."
    
    if "life story" in text:
        reply = predefined_answers["life story"]
    elif "superpower" in text:
        reply = predefined_answers["superpower"]
    elif "top 3 areas" in text:
        reply = predefined_answers["top 3 areas"]
    elif "misconceptions" in text:
        reply = predefined_answers["misconceptions"]
    elif "boundaries" in text:
        reply = predefined_answers["boundaries"]
    
    # Add messages to chat history
    st.session_state.history.append({"user": user_input, "bot": reply})
    
    # Speak the reply
    engine.say(reply)
    engine.runAndWait()

# Display chat history
for chat in st.session_state.history:
    message(chat["user"], is_user=True)
    message(chat["bot"])
