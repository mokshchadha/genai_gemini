from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
import time

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize session state for chat history if it doesn't exist
if "messages" not in st.session_state:
    st.session_state.messages = []

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    chunks = text_splitter.split_text(text)
    return chunks

def get_vector_store(text_chunks):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    vector_store.save_local("faiss_index")

def get_conversational_chain():
    prompt_template = """
    Answer the asked question as detailed as possible from the provided context, make sure to provide all the details, if the answer is 
    not available just say "answer is not available in the context", do not provide the wrong answer
    Context: {context}
    Question: {question}

    Answer:
    """
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    
    try:
        db = FAISS.load_local('faiss_index', embeddings, allow_dangerous_deserialization=True)
    except Exception as e:
        st.error("Please upload and process PDF files first!")
        return None
    
    llm = ChatGoogleGenerativeAI(model='gemini-1.5-pro', temperature=0.3)
    
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=db.as_retriever(),
        chain_type_kwargs={"prompt": prompt}
    )
    
    return qa_chain

def handle_user_input(user_question):
    qa_chain = get_conversational_chain()
    if qa_chain:
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": user_question})
        
        # Show typing indicator
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            message_placeholder.text("Thinking...")
            
            # Get response from chain
            response = qa_chain.invoke({"query": user_question})
            
            # Remove typing indicator and add assistant's response
            message_placeholder.empty()
            st.write(response['result'])
        
        # Add assistant's response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response['result']})

def create_chat_interface():
    # Custom CSS for chat interface
    st.markdown("""
        <style>
        .stChatMessage {
            padding: 1rem;
            border-radius: 0.5rem;
            margin-bottom: 1rem;
            max-width: 80%;
        }
        .user-message {
            background-color: #e6f3ff;
            margin-left: auto;
        }
        .assistant-message {
            background-color: #f0f0f0;
            margin-right: auto;
        }
        .chat-container {
            height: 600px;
            overflow-y: auto;
            padding: 1rem;
        }
        </style>
    """, unsafe_allow_html=True)

def main():
    st.set_page_config(
        page_title="Chat with Resumes",
        page_icon="📄",
        layout="wide"
    )

    # Create two columns: sidebar and main content
    with st.sidebar:
        st.title("📚 Pippin Documents")
        pdf_docs = st.file_uploader(
            "Upload your PDF files",
            accept_multiple_files=True,
            help="Select one or more PDF files to analyze"
        )
        
        if st.button("Process Documents", key="process_docs"):
            if pdf_docs:
                with st.spinner("Processing documents..."):
                    raw_text = get_pdf_text(pdf_docs)
                    text_chunks = get_text_chunks(raw_text)
                    get_vector_store(text_chunks)
                    st.success("✅ Documents processed successfully!")
                    st.session_state.messages = []  # Clear chat history when new documents are processed
            else:
                st.error("Please upload PDF files first!")
        
        # Add system status
        st.divider()
        st.subheader("System Status")
        try:
            if os.path.exists("faiss_index"):
                st.success("Vector Store: Ready")
            else:
                st.warning("Vector Store: Not initialized")
        except Exception as e:
            st.error(f"Error checking system status: {str(e)}")

    # Main chat interface
    st.title("💬 Chat with Your Documents")
    
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    # Chat input
    if user_question := st.chat_input("Ask me anything about the documents..."):
        if not os.path.exists("faiss_index"):
            st.error("Please upload and process PDF files first!")
        else:
            handle_user_input(user_question)

    # Add helpful instructions
    with st.expander("ℹ️ How to use this app"):
        st.markdown("""
        1. Upload your PDF documents using the sidebar
        2. Click 'Process Documents' to analyze them
        3. Start asking questions about your documents
        4. The AI will respond based on the content of your documents
        
        **Note**: Make sure to process your documents before starting the chat!
        """)

    # Security warning
    st.sidebar.divider()
    st.sidebar.warning("""
    ⚠️ Security Notice:
    - Only upload documents you have permission to use
    - This app stores data locally
    - Don't upload sensitive information
    """)

if __name__ == "__main__":
    main()