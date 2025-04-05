import streamlit as st
import openai

# Set up OpenAI API Key
openai.api_key = "YOUR_API_KEY"

st.set_page_config(page_title="AI Support Assistant", page_icon="💬", layout="wide")

# Wider layout styling
st.markdown("""
    <style>
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
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
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
    <div style='text-align: center; padding: 10px 0;'>
        <h1 style='color: #4B8BBE;'>🤖 AI Customer Support Assistant</h1>
        <p style='font-size:20px;'>Instantly get answers to your support queries.</p>
    </div>
""", unsafe_allow_html=True)

# Input area
with st.form(key="chat_form"):
    user_query = st.text_input("Type your question below 👇", placeholder="e.g. How can I reset my password?")
    submit = st.form_submit_button("🔍 Get Answer")

# AI Response
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
        st.success("✅ AI Response:")
        st.markdown(f"<div style='background-color:#f0f2f6;padding:15px;border-radius:10px;font-size:17px'>{ai_reply}</div>", unsafe_allow_html=True)

# Suggestions
with st.expander("💡 Need Suggestions?"):
    st.write("Try asking:")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.button("🔑 How do I change my password?")
    with col2:
        st.button("📦 Where is my order?")
    with col3:
        st.button("🕒 What are your working hours?")

# Footer
st.markdown("""
    <hr>
    <p style='text-align: center; font-size: 14px;'>Built with ❤️ by <b>Sakshi Kotur</b> | © 2025</p>
""", unsafe_allow_html=True)

