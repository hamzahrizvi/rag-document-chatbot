import os
import re
import time
import shutil
import tempfile
import streamlit as st
from langchain_core.documents import Document
from langchain_ollama import OllamaLLM, OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS

VECTOR_STORE_PATH = "vector_store"
LLM_MODEL = "mistral-nemo"
EMBED_MODEL = "nomic-embed-text"

st.set_page_config(page_title="RAG Chatbot", layout="wide")
st.title("RAG Document Chatbot")

embeddings = OllamaEmbeddings(model=EMBED_MODEL)

if "db" not in st.session_state:
    st.session_state.db = None

if "db_loaded" not in st.session_state:
    st.session_state.db_loaded = False


def load_existing_vector_store():
    if os.path.exists(VECTOR_STORE_PATH):
        try:
            db = FAISS.load_local(
                VECTOR_STORE_PATH,
                embeddings,
                allow_dangerous_deserialization=True
            )
            st.session_state.db = db
            st.session_state.db_loaded = True
            return True
        except Exception as e:
            st.error(f"Failed to load saved vector store: {e}")
    return False


def save_vector_store(db):
    db.save_local(VECTOR_STORE_PATH)


def build_documents_from_text(text):
    documents = [Document(page_content=text)]

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=400,
        chunk_overlap=40
    )

    return splitter.split_documents(documents)


def process_uploaded_file(uploaded_file):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".txt") as tmp:
        tmp.write(uploaded_file.read())
        temp_path = tmp.name

    try:
        with open(temp_path, "r", encoding="utf-8", errors="ignore") as f:
            text = f.read().strip()

        if not text:
            st.error("Uploaded file is empty.")
            return

        chunks = build_documents_from_text(text)

        if os.path.exists(VECTOR_STORE_PATH):
            db = FAISS.load_local(
                VECTOR_STORE_PATH,
                embeddings,
                allow_dangerous_deserialization=True
            )
            db.add_documents(chunks)
        else:
            db = FAISS.from_documents(chunks, embeddings)

        save_vector_store(db)
        st.session_state.db = db
        st.session_state.db_loaded = True
        st.success("File processed and saved to the local knowledge base.")

    except Exception as e:
        st.error(f"File processing error: {e}")

    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)


def extract_credentials(context):
    username_match = re.search(r"Username:\s*(.+)", context, re.IGNORECASE)
    password_match = re.search(r"Password:\s*(.+)", context, re.IGNORECASE)

    if username_match and password_match:
        username = username_match.group(1).strip()
        password = password_match.group(1).strip()
        return f"Username: {username}\nPassword: {password}"

    return None


def is_credentials_query(query):
    q = query.lower().strip()

    strong_patterns = [
        "default credentials",
        "login credentials",
        "default login",
        "username and password",
        "what is the username",
        "what is the password",
        "what are the credentials",
        "what are the default credentials",
    ]

    return any(p in q for p in strong_patterns)


def answer_query(query):
    t1 = time.time()
    docs = st.session_state.db.similarity_search(query, k=3)
    t2 = time.time()

    if not docs:
        return "I could not find that in the knowledge base.", "", t2 - t1, 0.0

    context = "\n\n".join(doc.page_content for doc in docs)

    if is_credentials_query(query):
        creds = extract_credentials(context)
        if creds:
            t3 = time.time()
            return creds, context, t2 - t1, t3 - t2

    llm = OllamaLLM(model=LLM_MODEL)

    prompt = f"""Answer the user's question using only the context below.

Instructions:
- Answer clearly and directly.
- If the context contains steps, summarize the relevant steps.
- If the answer is not present in the context, say exactly: I could not find that in the knowledge base.
- Do not invent details.
- Do not add unrelated advice or examples.

Context:
{context}

Question: {query}

Answer:
"""

    response = llm.invoke(prompt).strip()
    t3 = time.time()

    if not response:
        response = "I could not find that in the knowledge base."

    return response, context, t2 - t1, t3 - t2


if not st.session_state.db_loaded:
    load_existing_vector_store()

uploaded_file = st.file_uploader("Upload a .txt file", type=["txt"])

col1, col2 = st.columns([3, 1])

with col1:
    if uploaded_file is not None:
        process_uploaded_file(uploaded_file)

with col2:
    if st.button("Clear knowledge base"):
        if os.path.exists(VECTOR_STORE_PATH):
            shutil.rmtree(VECTOR_STORE_PATH)

        st.session_state.db = None
        st.session_state.db_loaded = False
        st.success("Local knowledge base cleared.")

if st.session_state.db is not None:
    st.info("Knowledge base loaded and ready.")
else:
    st.warning("No saved knowledge base found. Upload a file to create one.")

with st.form("question_form"):
    query = st.text_input("Ask a question about your knowledge base")
    submitted = st.form_submit_button("Submit")

if submitted:
    if st.session_state.db is None:
        st.warning("Upload a file first.")
    elif not query.strip():
        st.warning("Enter a question.")
    else:
        try:
            response, context, retrieval_time, llm_time = answer_query(query)

            st.write(f"Retrieval time: {retrieval_time:.2f}s")
            st.write(f"LLM time: {llm_time:.2f}s")

            st.subheader("Answer")
            st.write(response)

            with st.expander("Retrieved context"):
                st.write(context)

        except Exception as e:
            st.error(f"Response generation error: {e}")