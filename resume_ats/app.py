from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
os.environ['PATH'] += ':/opt/homebrew/bin'
import io
import base64

from PIL import Image

import pdf2image
import google.generativeai as genai

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
model = genai.GenerativeModel('gemini-1.5-pro')

def get_gemini_response(input, pdf_content, prompt):
    response = model.generate_content([input, pdf_content[0], prompt])
    return response.text

def input_pdf_setup(uploaded_file):
    ## converting the pdf to image
    if uploaded_file is not None:
        images = pdf2image.convert_from_bytes(uploaded_file.read())
        first_page = images[0]

        ## converting image to bytes
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format="JPEG")
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()
            }
        ]

        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")




st.set_page_config(page_title="ATS resume expert")

st.header("ATS writing system")
text_input = st.text_area("Job description: ", key="input")

uploaded_file=st.file_uploader("Upload your resume in PDF ...", type=['pdf'])

submit1 = st.button("Tell me about the resume")
submit2 = st.button("How can i improvise my skills")
submit3 = st.button("Percentage match")


input_prompt1 = '''
    You are an experienced technical human resource manager, your task is to review 
    the provided resume against the job description
    please share your professional evaluation on whether the candidate's profile aligns with the Job description or not
    Highlight the strengths and weaknesses of the applicant in relation to the specific role. 
'''

input_prompt2 = '''
    You are an technical Human resource manger with expertise in data science,
    your role is to scrutinize the resume in light of the job description provided.
    Share your insights on the candidate's suitability for the role from an HR 
    Additionally, offer advice on enhancing the candidate's skills and identify any weaknesses.
'''

input_prompt3 = '''
    You are an skilled ATS (Application tracking system) scanner with deep understanding of the Data Science, Web Development, Mobile development,
    Big Data Engineering, Devops, Data analyst and deep ATS functionality
    your task is to evaluate the resume against the provided job description give me the percentage the job description. First the output should come as percentage and then
    keywords missing .
'''

if submit1:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt1, pdf_content, text_input)
        st.write(response)
    else:
        st.write("Please upload resume")
    

if submit2:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt2, pdf_content, text_input)
        st.write(response)
    else:
        st.write("Please upload resume")

if submit3:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt3, pdf_content, text_input)
        st.write(response)
    else:
        st.write("Please upload resume")