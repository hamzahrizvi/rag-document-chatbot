
---

# 2. ✅ **Iteration / Issues & Solutions Document**

# Iteration Log

## v1 → v2 Improvements

---

### Issue: No persistence
**Problem**
- Documents had to be re-uploaded every session

**Solution**
- Implemented FAISS local storage using `save_local()` and `load_local()`

---

### Issue: Poor retrieval accuracy
**Problem**
- Irrelevant chunks retrieved
- Model hallucinated answers

**Root Cause**
- Used LLM model for embeddings (`phi` / `mistral`)

**Solution**
- Switched to dedicated embedding model: `nomic-embed-text`
- Rebuilt vector store

---

### Issue: Hallucinated answers
**Problem**
- Model generated incorrect credentials and fabricated content

**Solution**
- Improved prompt structure
- Added instruction constraints (no guessing, context-only)
- Reduced retrieved context size (k=2–3)

---

### Issue: Over-restrictive responses
**Problem**
- Responses too short or empty
- Model refused valid answers

**Solution**
- Balanced prompt to allow both factual and procedural responses
- Removed overly strict rules

---

### Issue: Incorrect repeated answers
**Problem**
- Credential extraction triggered for unrelated queries

**Solution**
- Refined query detection logic
- Limited extraction to explicit credential queries

---

### Issue: Streamlit requiring multiple submits
**Problem**
- App required pressing submit twice

**Solution**
- Replaced button with `st.form` submission
- Stabilized state handling

---

### Issue: Slow or inconsistent responses
**Problem**
- High latency and inconsistent outputs

**Solution**
- Switched to better LLM (`mistral-nemo`)
- Reduced chunk size and overlap
- Limited retrieval size

---

## Current Limitations

- Single file ingestion
- No metadata filtering
- No memory or conversational context
- No ranking or reranking layer

---

## Planned Improvements (v3)

- Multi-document ingestion
- Persistent metadata tagging
- Reranking (better retrieval quality)
- Chat memory
- UI improvements
- Evaluation metrics (answer correctness)
