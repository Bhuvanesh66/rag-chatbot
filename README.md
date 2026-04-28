# 📄 Multilingual PDF Chatbot (Grounded RAG System)

## 🚀 Overview

This project is a **PDF-Constrained Conversational Agent** that:

* Answers questions strictly from a given PDF
* Provides **page-number citations**
* Refuses out-of-scope queries
* Supports **multiple languages**

---

## ✅ Features

* 📄 PDF Upload & Processing
* 🔍 Semantic Search using FAISS
* 🌐 Multilingual Support
* ❌ Strict Refusal for Out-of-Scope Queries
* 📚 Citation-based Answers (Page Numbers)
* 💬 Conversational Memory

---

## 🧠 Tech Stack

* Streamlit (UI)
* FAISS (Vector Search)
* Sentence Transformers (Embeddings)
* Azure OpenAI API (LLM)

---

## ⚙️ Setup Instructions

### 1. Clone Repo

```bash
git clone https://github.com/Bhuvanesh66/rag-chatbot.git
cd rag-chatbot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Add API Key

Create `.env` file:

```
GITHUB_TOKEN=your_api_key
```

### 4. Run App

```bash
streamlit run app.py
```

---

## 🧪 Sample Test Queries

### ✅ Valid Queries

* What is the main objective?
* Summarize page 2
* इस दस्तावेज़ का उद्देश्य क्या है?
* ಈ ಡಾಕ್ಯುಮೆಂಟ್‌ನ ಮುಖ್ಯ ಉದ್ದೇಶ ಏನು?

### ❌ Invalid Queries

* Who is the president of India?
* Explain React
* What is quantum physics?

👉 Expected Output:

```
Not found in document
```

---

## 🏆 Evaluation Criteria Covered

* Grounded responses
* Citation accuracy
* Hallucination prevention
* Multilingual consistency

---

