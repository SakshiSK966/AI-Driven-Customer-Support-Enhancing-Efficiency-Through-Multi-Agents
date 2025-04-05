import streamlit as st
import openai
from streamlit.components.v1 import html

# Replace with your actual OpenAI API Key
openai.api_key = "YOUR_API_KEY"

st.set_page_config(page_title="Smart AI Support Assistant", page_icon="💬", layout="centered")

st.markdown("""
    <style>
        .main {
            background-color: #f4f9ff;
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        .stTextInput>div>div>input {
            padding: 0.75rem;
            border-radius: 10px;
            border: 1px solid #ccc;
        }
        .stButton>button {
            background-color: #4a90e2;
            color: white;
            padding: 0.75rem 1.5rem;
            border-radius: 10px;
            border: none;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

st.title("💬 Smart AI Support Assistant")
st.subheader("Talk or type to get instant customer support answers!")

st.markdown("#### 🎙️ Speak below:")

# JavaScript for browser mic input
html_code = """
<script>
const streamlitSpeech = window.streamlitSpeech || {};
streamlitSpeech.recognize = function() {
    var recognition = new webkitSpeechRecognition();
    recognition.lang = "en-US";
    recognition.continuous = false;
    recognition.interimResults = false;

    recognition.onresult = function(event) {
        const text = event.results[0][0].transcript;
        window.parent.postMessage({ type: 'streamlit:speech', text: text }, '*');
    };

    recognition.onerror = function(event) {
        window.parent.postMessage({ type: 'streamlit:speech', text: "ERROR" }, '*');
    };

    recognition.start();
};
</script>
<button onclick="streamlitSpeech.recognize()">🎤 Start Speaking</button>
"""

html(html_code, height=100)

# Listen for result
speech_text = st.experimental_get_query_params().get("voice", [None])[0]
if "_streamlit_messages" in st.session_state:
    for m in st.session_state["_streamlit_messages"]:
        if m["type"] == "streamlit:speech":
            speech_text = m["text"]

user_query = ""
if speech_text and speech_text != "ERROR":
    st.success(f"You said: {speech_text}")
    user_query = speech_text
elif speech_text == "ERROR":
    st.error("Could not understand. Try again.")

# Manual text input
typed_input = st.text_input("💬 Or type your question:")
if typed_input:
    user_query = typed_input

# AI Response
if st.button("Get Answer") and user_query:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful customer support agent."},
            {"role": "user", "content": user_query}
        ]
    )
    st.markdown("### 🤖 AI Response:")
    st.write(response["choices"][0]["message"]["content"])

st.markdown("---")
st.markdown("<p style='text-align:center;'>🚀 Created by <b>Sakshi Kotur</b> | 2025</p>", unsafe_allow_html=True)
