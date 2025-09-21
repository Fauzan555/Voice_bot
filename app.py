import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Voice Chatbot Demo", page_icon="🤖")

st.title("Voice Chatbot Demo")
st.write("Ask any of the sample questions below:")

st.markdown("""
- What should we know about your life story in a few sentences?  
- What’s your #1 superpower?  
- What are the top 3 areas you’d like to grow in?  
- What misconception do your coworkers have about you?  
- How do you push your boundaries and limits?  
""")

# Predefined answers
predefined_answers = {
    "life story": "I’m an AI model designed to assist and provide information. I learn continuously and love helping people solve problems in creative ways.",
    "superpower": "Understanding and generating human-like text to make communication seamless and insightful.",
    "top 3 areas": "I aim to improve real-time reasoning, creative problem-solving, and understanding complex emotions in human conversation.",
    "misconceptions": "People sometimes think I have personal experiences or feelings, but I generate responses based on patterns in data.",
    "boundaries": "I experiment with new types of questions and domains to improve my accuracy and usefulness continuously."
}

if 'history' not in st.session_state:
    st.session_state.history = []

user_input = st.text_input("Type your question here:")

if st.button("Ask"):
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

    st.session_state.history.append({"user": user_input, "bot": reply})

# Show chat history
for chat in st.session_state.history:
    st.markdown(f"**You:** {chat['user']}")
    st.markdown(f"**Bot:** {chat['bot']}")

    # 🔊 Use browser speech synthesis for bot reply
    components.html(
        f"""
        <script>
        var msg = new SpeechSynthesisUtterance("{chat['bot']}");
        window.speechSynthesis.speak(msg);
        </script>
        """,
        height=0,
    )
    st.markdown("---")
