import openai
import streamlit as st
import speech_recognition as sr

# Set your OpenAI API key
from config.config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def get_openai_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message['content']

def voice_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("कृपया बोलें...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio, language='hi-IN')
            st.write(f"आपने कहा: {command}")
            return command
        except sr.UnknownValueError:
            st.write("मुझे आपकी आवाज़ समझ में नहीं आई। कृपया फिर से प्रयास करें।")
            return None

st.title("AI Help Assistant")
if st.button("वॉयस कमांड"):
    user_input = voice_command()
else:
    user_input = st.text_input("Ask your question:")
    
if st.button("Submit"):
    if user_input:
        answer = get_openai_response(user_input)
        st.write(answer)
    else:
        st.write("Please enter a question.")
