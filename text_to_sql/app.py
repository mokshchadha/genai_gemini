from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os 
import sqlite3

import google.generativeai as genai 
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(question, prompts):
    model=genai.GenerativeModel('gemini-1.5-pro')
    response=model.generate_content([prompts[0], question])
    return response.text

def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    curr = conn.cursor()
    curr.execute(sql)
    rows = curr.fetchall()
    conn.commit()
    conn.close()

    for row in rows:
        print(row)
    return rows



## Define your prompt
prompts = ['''
    You are an expert in converting English question to SQL query!
    The SQL database has the table name Student and has the following columns - NAME, CLASS, SECTION, MARKS
    For example :- 
    Example 1 : How many records are present? , The SQL command will be SELECT * from STUDENT;
    Example 2 : Tell me all the students studying in Data Science class?, the SQL command will be something like this SELECT * from STUDENT where CLASS = "Data Science";

    also the sql code should not have ``` in the beginning or end and sql word in out.
'''

]

### STREAM LIT APP
st.set_page_config(page_title="SQL")
st.header("Gemini App To Retrieve SQL Data")

question=st.text_input("Input: ", key="input")
submit = st.button("Ask the question")

if submit :
    response = get_gemini_response(question, prompts)
    print(response)

    data = read_sql_query(response, "student.db")
    st.subheader("The response is ")
    for row in data:
        st.write(row)