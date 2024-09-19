from dotenv import load_dotenv
load_dotenv()
import os
import streamlit as st
import google.generativeai as genai


apiKey = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=apiKey)
model = genai.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat(history=[])

def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response

## streamlit app

st.set_page_config(page_title="Q&A Demo")
st.header("Gemini LLM Application")

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = [] #initializing if does not exist

my_input=st.text_input("Input: ", key="input")
submit=st.button("Ask the question")

if submit and my_input:
    response = get_gemini_response(my_input)
    ## add user query response to the history 
    st.session_state['chat_history'].append(("You", my_input))
    st.subheader("The response is")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot", chunk.text))
    

st.subheader("The chat history")
for role,text in st.session_state['chat_history']:
    st.write(f"{role}:{text}")