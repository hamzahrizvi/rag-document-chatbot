import streamlit as st
from langchain_community.llms import Ollama
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OllamaEmbeddings
import tempfile

st.set_page_config(page_title="RAG Chatbot", layout="wide")
st.header("RAG Document Chatbot")

uploaded_file = st.file_uploader("Upload a .txt file", type=["txt"])

if "db" not in st.session_state:
    st.session_state.db = None

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(uploaded_file.read())
        temp_path = tmp.name

    loader = TextLoader(temp_path)
    docs = loader.load()

    embeddings = OllamaEmbeddings(model="phi")
    db = FAISS.from_documents(docs, embeddings)

    st.session_state.db = db
    st.success("File processed. Ask a question.")

query = st.text_input("Ask a question about your file")

if st.button("Submit") and query:
    if st.session_state.db is None:
        st.warning("Upload a file first.")
    else:
        results = st.session_state.db.similarity_search(query)
        context = "\n".join([doc.page_content for doc in results])

        llm = Ollama(model="phi")
        response = llm.invoke(
            f"Answer only from this context:\n\n{context}\n\nQuestion: {query}"
        )

        st.write(response)