import tempfile
import streamlit as st
from langchain_core.documents import Document
from langchain_ollama import OllamaLLM, OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS

st.set_page_config(page_title="RAG Chatbot", layout="wide")
st.title("RAG Document Chatbot")

uploaded_file = st.file_uploader("Upload a .txt file", type=["txt"])

if "db" not in st.session_state:
    st.session_state.db = None

if uploaded_file is not None:
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".txt") as tmp:
            tmp.write(uploaded_file.read())
            temp_path = tmp.name

        with open(temp_path, "r", encoding="utf-8", errors="ignore") as f:
            text = f.read().strip()

        if not text:
            st.error("Uploaded file is empty.")
        else:
            documents = [Document(page_content=text)]

            splitter = RecursiveCharacterTextSplitter(
                chunk_size=500,
                chunk_overlap=50
            )
            chunks = splitter.split_documents(documents)

            embeddings = OllamaEmbeddings(model="phi")
            db = FAISS.from_documents(chunks, embeddings)

            st.session_state.db = db
            st.success("File processed. Ask a question.")

    except Exception as e:
        st.error(f"File processing error: {e}")

query = st.text_input("Ask a question about your file")

if st.button("Submit"):
    if st.session_state.db is None:
        st.warning("Upload a file first.")
    elif not query.strip():
        st.warning("Enter a question.")
    else:
        try:
            docs = st.session_state.db.similarity_search(query, k=3)
            context = "\n\n".join(doc.page_content for doc in docs)

            llm = OllamaLLM(model="phi")

            prompt = f"""You must answer using only the context below.
If the answer is not in the context, say: "I could not find that in the uploaded file."

Context:
{context}

Question: {query}

Answer:
"""

            response = llm.invoke(prompt)

            st.subheader("Answer")
            st.write(response)

            with st.expander("Retrieved context"):
                st.write(context)

        except Exception as e:
            st.error(f"Response generation error: {e}")