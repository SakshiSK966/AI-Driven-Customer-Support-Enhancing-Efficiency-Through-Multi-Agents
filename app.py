import streamlit as st
import openai

# Set up OpenAI API key (Replace 'YOUR_API_KEY' with your actual key)
openai.api_key = "YOUR_API_KEY"

def get_ai_response(user_query):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You are a helpful customer support agent."},
                  {"role": "user", "content": user_query}]
    )
    return response["choices"][0]["message"]["content"].strip()

# Streamlit UI
st.title("AI-Driven Customer Support")
st.write("Ask any question related to customer support!")

user_query = st.text_input("Your Question:")

if st.button("Get Answer") and user_query:
    response = get_ai_response(user_query)
    st.write("**AI Response:**", response)
