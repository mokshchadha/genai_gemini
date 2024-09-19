from dotenv import load_dotenv
load_dotenv()

import os
import streamlit as st
import google.generativeai as genai
from PIL import Image

# Configure the Google Generative AI
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
model = genai.GenerativeModel('gemini-1.5-flash')  # Retained original model name

def get_gemini_response(input_prompt, image, user_prompt):
    response = model.generate_content([input_prompt, image, user_prompt])
    return response.text

def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image = Image.open(uploaded_file)
        return image
    else:
        raise FileNotFoundError("No file uploaded")

# Streamlit app
st.set_page_config(page_title="Multi-language Invoice Extractor")
st.header("Invoice Analysis with Gemini")

input_prompt = """
You are an expert in understanding invoices. When an image is uploaded, 
you will analyze it and answer questions based on the invoice contents.
"""

user_prompt = st.text_input("Ask a question about the invoice:", key="input")
uploaded_file = st.file_uploader("Upload an image of the invoice...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Invoice", use_column_width=True)

submit = st.button("Analyze Invoice")

if submit:
    if uploaded_file is None:
        st.error("Please upload an invoice image before submitting.")
    else:
        with st.spinner("Analyzing the invoice..."):
            image = input_image_setup(uploaded_file)
            response = get_gemini_response(input_prompt, image, user_prompt)
            st.subheader("Analysis Result")
            st.write(response)