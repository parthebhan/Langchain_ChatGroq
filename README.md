# **ChatGroq: An AI-Powered Information Hub**

### Purpose

The code creates a Streamlit application (`app.py`) that allows users to interact with content extracted from a webpage. Users can input a URL, initialize a vector store from the webpage content, and then query the content using AI techniques. The app utilizes embeddings, similarity search, and a conversational AI model for generating responses.


[![Streamlit App](https://img.shields.io/badge/Streamlit_App_-Langchain_PDF_Reader-ff69b4.svg?style=for-the-badge&logo=Streamlit)](https://langchainragwebpagefaisschatgroq-qmewpejud3jortzh6stoa5.streamlit.app/)

### Dependencies

- **Streamlit**: For building the interactive web interface.
- **langchain_groq**: For integrating ChatGroq for conversational AI.
- **langchain_community**: For document loaders and vector stores.
- **langchain_google_genai**: For text embeddings using Google's Generative AI.
- **langchain_core**: For prompt templates and chains.
- **time**: For measuring response time.

### Main Functions and Workflow

1. **Initialize Components**:
   - **Purpose**: Initialize embeddings, document loaders, and vector store.
   - **Implementation**: Uses `GoogleGenerativeAIEmbeddings` for embeddings and `FAISS` for vector store creation. Documents are loaded from the provided URL and split into chunks for processing.

2. **ChatGroq Instance**:
   - **Purpose**: Setup ChatGroq for generating responses.
   - **Implementation**: Initializes ChatGroq with API key and model name.

3. **Chat Prompt Template**:
   - **Purpose**: Defines the prompt template for generating answers.
   - **Implementation**: Uses `ChatPromptTemplate` to create a template for the conversational AI model.

4. **Document and Retrieval Chains**:
   - **Purpose**: Setup chains for processing documents and retrieving relevant information.
   - **Implementation**: Uses `create_stuff_documents_chain` and `create_retrieval_chain` to handle document processing and retrieval.

5. **User Input Handling**:
   - **Purpose**: Handle user queries and generate responses.
   - **Implementation**: Uses the initialized retrieval chain to process user queries and provide answers. Displays document similarity search results.

6. **Reset Functionality**:
   - **Purpose**: Reset the app state.
   - **Implementation**: Clears all session state variables to allow fresh interactions.

### Usage

1. **Input URL**: Users provide a webpage URL to load and process content.
2. **Submit and Process**: Initializes the vector store with the content from the provided URL.
3. **Ask Questions**: Users input questions related to the content. The AI model provides responses based on the processed content.
4. **Reset**: Clears the app state and allows users to start fresh.

### Summary

The app integrates various AI techniques to interact with and query content from webpages. It handles text extraction, processing, and question answering through an intuitive web interface.

### Author

This app was created by `Parthebhan Pari`.

### Notes

- This app uses the Gemini Pro model from Google's GenerativeAI API for generating responses.
- Ensure that you have a stable internet connection to interact with the Gemini Pro model.
- For security reasons, handle and store your API key securely.

### Connect with Me

Feel free to connect with me on:
- [Portfolio](#)
- [LinkedIn Profile](#)
- [Kaggle Profile](#)
- [Tableau Profile](#)



## 🔗 Connect with Me

Feel free to connect with me on LinkedIn:

[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://parthebhan143.wixsite.com/datainsights)

[![LinkedIn Profile](https://img.shields.io/badge/LinkedIn_Profile-000?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/parthebhan)

[![Kaggle Profile](https://img.shields.io/badge/Kaggle_Profile-000?style=for-the-badge&logo=kaggle&logoColor=white)](https://www.kaggle.com/parthebhan)

[![Tableau Profile](https://img.shields.io/badge/Tableau_Profile-000?style=for-the-badge&logo=tableau&logoColor=white)](https://public.tableau.com/app/profile/parthebhan.pari/vizzes)

