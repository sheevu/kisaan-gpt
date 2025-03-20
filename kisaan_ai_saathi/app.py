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

# Home Screen
st.title("Kisaan Sathi GPT")
st.write("Indian Farmers Increase Income and Improve Agricultural Practices")
st.subheader("Developed by Sudarshan AI Labs")

# Language Toggle
language = st.selectbox("Select Language:", ["English", "हिन्दी"])

# Navigation Menu
st.sidebar.title("Navigation")
menu_options = ["Home", "Resources", "AI Assistant", "Community Forum"]
selected_menu = st.sidebar.selectbox("Select Menu", menu_options)

# Display Logo
st.image("https://example.com/valid_logo.png", caption="Kisaan Sathi GPT Logo")  # Replace with a valid logo URL

# Initialize session state for conversation history
if 'conversation_history' not in st.session_state:
    st.session_state.conversation_history = []

# AI Assistant Section
if selected_menu == "AI Assistant":
    st.header("AI Assistant")
    st.write("Ask your questions related to agriculture.")
    
    # Location Input
    location = st.selectbox("Select your location:", ["Uttar Pradesh", "Madhya Pradesh", "Haryana", "Punjab"])
    st.write(f"Selected Location: {location}")

    st.write("कृपया अपने प्रश्न टाइप करें:")
    user_input = st.text_input("आपका प्रश्न / Your Question:", key="text_input_1")

    # Add a submit button next to the text input
    if st.button("Submit"):
        if user_input:
            # Modify prompt to include location context
            prompt_with_location = f"{user_input} in {location}"
            answer = get_openai_response(prompt_with_location)
            st.write(answer)

            # Store the conversation in session state
            st.session_state.conversation_history.append({"user": user_input, "bot": answer})
        else:
            st.write("Please enter a question.")

    # Display conversation history
    if st.session_state.conversation_history:
        st.subheader("Conversation History")
        for chat in st.session_state.conversation_history:
            st.write(f"User: {chat['user']}")
            st.write(f"Bot: {chat['bot']}")

    # Add examples of questions farmers can ask
    st.write("Examples of questions you can ask:")
    st.write("- What is the weather like?")
    st.write("- What are the current crop prices?")
    st.write("- How can I control pests?")

    # Add new buttons
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

    if st.button("Chat"):
        st.write("Chat functionality will be implemented here.")

# Resource Hub Section
elif selected_menu == "Resources":
    st.header("Resource Hub")
    st.write("Explore articles, videos, and tutorials.")
    # Placeholder for resource content
    st.write("Resource content will be displayed here.")

# Community Forum Section
elif selected_menu == "Community Forum":
    st.header("Community Forum")
    st.write("Join discussions and share knowledge.")
    # Placeholder for forum content
    st.write("Forum content will be displayed here.")

# Add visual elements
st.image("https://example.com/valid_farm_image.png", caption="Farm Image", use_container_width=True)  # Replace with a valid farm image URL

# Voice Input Option
if st.button("TALK", key="talk"):
    user_input = voice_command()

# Debug Panel
if st.session_state.get('debug', False):
    st.sidebar.write("Debug Mode: OpenAI is responding...")
