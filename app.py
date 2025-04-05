import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = "YOUR_API_KEY"

# Page config and styling
st.set_page_config(page_title="AI Support Assistant", page_icon="💬", layout="wide")

st.markdown("""
    <style>
        .block-container {
            padding-top: 2rem;
            padding-bottom: 5rem;
            max-width: 95%;
        }
        .stTextInput>div>div>input {
            font-size: 18px;
            padding: 0.75rem;
        }
        .stButton>button {
            font-size: 16px;
            padding: 0.6rem 1.2rem;
            background-color: #4B8BBE;
            color: white;
            border-radius: 10px;
            border: none;
        }
        .response-box {
            background-color: #f0f2f6;
            padding: 20px;
            border-radius: 10px;
            font-size: 17px;
            min-height: 150px;
        }
        hr {
            margin-top: 4rem;
            margin-bottom: 2rem;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("""
    <div style='text-align: center; padding: 20px 0;'>
        <h1 style='color: #4B8BBE;'>🤖 AI Customer Support Assistant</h1>
        <p style='font-size:20px;'>Get help instantly from an intelligent AI assistant</p>
    </div>
""", unsafe_allow_html=True)

# Input
with st.form(key="chat_form"):
    st.markdown("### 💬 Ask your question:")
    user_query = st.text_input("", placeholder="e.g. How do I reset my password?")
    submit = st.form_submit_button("🔍 Get Answer")

# Response
if submit and user_query:
    with st.spinner("Generating answer..."):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful customer support agent."},
                {"role": "user", "content": user_query}
            ]
        )
        ai_reply = response["choices"][0]["message"]["content"].strip()
        st.markdown("### ✅ AI Response:")
        st.markdown(f"<div class='response-box'>{ai_reply}</div>", unsafe_allow_html=True)

# Space for visual height
st.markdown("### ℹ️ Need help? Try these examples:")
st.write("- 🔒 How to change my password?")
st.write("- 🚚 Where is my order?")
st.write("- 🕒 What are your working hours?")
st.write("- 📧 How do I contact support?")
st.write("- 💳 How to update billing info?")

# Extra vertical space
for _ in range(10):
    st.write("")

# Footer
st.markdown("""
    <hr>
    <p style='text-align: center; font-size: 14px;'>Built with ❤️ by <b>Sakshi Kotur</b> | © 2025</p>
""", unsafe_allow_html=True)
