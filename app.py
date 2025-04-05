import streamlit as st
import openai
import speech_recognition as sr

# Replace with your actual OpenAI API Key
openai.api_key = "YOUR_API_KEY"

st.set_page_config(page_title="Smart AI Support Assistant", page_icon="💬", layout="centered")

# Styling
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

user_query = ""

# 🎙️ Voice Input Section
st.markdown("#### 🎙️ Press 'Start Listening' and speak your question:")

if st.button("Start Listening"):
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        st.info("Listening... Please speak now.")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        user_query = recognizer.recognize_google(audio)
        st.success(f"Recognized Speech: {user_query}")
    except sr.UnknownValueError:
        st.error("Sorry, I could not understand the audio.")
    except sr.RequestError:
        st.error("Could not request results; check your internet connection.")

# 💬 Text Input Section
st.markdown("#### 💬 Or type your question below:")
typed_input = st.text_input("Type your question here:")
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

