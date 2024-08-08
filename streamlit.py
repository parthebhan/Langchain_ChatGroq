import streamlit as st
import os
import time
from langchain_groq import ChatGroq
from langchain_community.document_loaders import WebBaseLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS

# Streamlit Secrets
GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
groq_api_key = st.secrets['GROQ_API_KEY']

# Streamlit UI
st.title("ChatGroq - Webpage URL - Ask Questions and Get Answers")

# Input for webpage URL
webpage_url = st.text_input("Enter the webpage URL")

# Initialize components if not already in session state
if "vectors" not in st.session_state:
    if webpage_url:
        try:
            embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
            loader = WebBaseLoader(webpage_url)
            docs = loader.load()

            text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
            final_documents = text_splitter.split_documents(docs[:50])
            vectors = FAISS.from_documents(final_documents, embeddings)
            st.write("Vector DB Ready , Enter the query below!")
            st.session_state.vectors = vectors
        except Exception as e:
            st.error(f"An error occurred: {e}")

# Initialize ChatGroq instance
llm = ChatGroq(groq_api_key=groq_api_key, model_name="mixtral-8x7b-32768")

# Chat prompt template
prompt = ChatPromptTemplate.from_template(
    """
    Answer the questions based on the provided context only.
    Please provide the most accurate response based on the question
    <context>
    {context}
    <context>
    Questions:{input}

    """
)

# Create document and retrieval chains
document_chain = create_stuff_documents_chain(llm, prompt)

# Check if vectors are initialized in session state
if "vectors" in st.session_state:
    retriever = st.session_state.vectors.as_retriever()
    retrieval_chain = create_retrieval_chain(retriever, document_chain)

    # Input prompt from user
    user_prompt = st.text_input("Input your prompt here")

    if user_prompt:
        start = time.time()
        try:
            response = retrieval_chain.invoke({"input": user_prompt})
            st.write(response['answer'])
            st.write("Response time:", time.time() - start)

            # Display document similarity search results in expander
            with st.expander("Document Similarity Search"):
                for i, doc in enumerate(response["context"]):
                    st.write(doc.page_content)
                    st.write("--------------------------------")
        except Exception as e:
            st.error(f"An error occurred while processing your request: {e}")

else:
    st.warning("Please enter a valid webpage URL to initialize document vectors.")

# Reset functionality
if st.button('Reset'):
    st.session_state.clear()  # Clears all session state variables
    st.write("App has been reset. Please enter a webpage URL again.")
