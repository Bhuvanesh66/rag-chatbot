import streamlit as st
import os
from dotenv import load_dotenv

from pdf_loader import load_and_split_pdf
from embedder import load_embedding_model, embed_texts
from retriever import VectorStore
from qa_chain import generate_answer

load_dotenv()

api_key = os.getenv("GITHUB_TOKEN")

if not api_key:
    st.error("⚠️ GITHUB_TOKEN not set!")
    st.stop()

st.title("📄 Multilingual Grounded PDF Chatbot")

# 🔹 session memory
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

uploaded_file = st.file_uploader("Upload PDF", type="pdf")

if uploaded_file:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    st.write("Processing PDF...")

    docs = load_and_split_pdf("temp.pdf")

    texts = [doc.page_content for doc in docs]
    metadatas = [doc.metadata for doc in docs]

    model = load_embedding_model()

    embeddings = embed_texts(model, texts)

    vector_store = VectorStore(len(embeddings[0]))
    vector_store.add(embeddings, texts, metadatas)

    st.success("Ready!")

    query = st.text_input("Ask a question")

    if query:
        query_embedding = model.encode([query])[0]

        results = vector_store.search(query_embedding, k=3)

        # ❌ STRONG REFUSAL (before LLM)
        if len(results) == 0 or max([r["score"] for r in results]) < 0.5:
            st.warning("❌ Not found in document")
            st.stop()
        context = "\n\n".join(
            [f"[Page {r['page']}]\n{r['text']}" for r in results]
        )

        answer = generate_answer(context, query, st.session_state.chat_history)

        # save history
        st.session_state.chat_history.append((query, answer))

        st.write("### Answer")
        st.write(answer)

        # show chat history
        with st.expander("💬 Conversation History"):
            for q, a in st.session_state.chat_history:
                st.write(f"**Q:** {q}")
                st.write(f"**A:** {a}")