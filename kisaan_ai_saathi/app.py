import openai
import streamlit as st

# Set your OpenAI API key
openai.api_key = "YOUR_API_KEY"

def get_openai_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message['content']

st.title("AI Help Assistant")
user_input = st.text_input("Ask your question:")
if st.button("Submit"):
    if user_input:
        answer = get_openai_response(user_input)
        st.write(answer)
    else:
        st.write("Please enter a question.")
