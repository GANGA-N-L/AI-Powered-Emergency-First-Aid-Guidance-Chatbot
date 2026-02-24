# 🚑 AI-Powered Emergency First Aid Guidance Chatbot

An AI-driven emergency assistant that provides first aid guidance using Retrieval-Augmented Generation (RAG) with local LLM support.

## 📌 Overview

This project is an AI-powered web application that provides first aid guidance during emergencies.

It uses:
- Retrieval-Augmented Generation (RAG)
- Vector search for medical manuals
- Local LLM inference via Ollama
- Flask web framework for backend
- HTML/CSS/JavaScript frontend

## ✨ Features

- 🔎 Context-aware medical guidance using RAG
- 📚 Knowledge sourced from first aid manuals (PDF)
- 🤖 Local LLM inference using Ollama (Phi)
- 🌐 Web-based interactive chat interface
- ⚡ Fast semantic search with Pinecone
- 📱 Responsive UI design

## 🛠 Tech Stack

- Python
- Flask
- LangChain
- Pinecone Vector Database
- Ollama (Phi model)
- HuggingFace Embeddings
- HTML, CSS, JavaScript

## 🧠 Architecture

User Query
    ↓
Flask Backend
    ↓
Retriever (Pinecone Vector Store)
    ↓
Relevant Document Chunks
    ↓
Local LLM (Ollama)
    ↓
Generated Response
    ↓
Frontend Display


## How to Run?

### 1️⃣ Clone the repository

```bash
git clone https://github.com/GANGA-N-L/AI-Powered-Emergency-First-Aid-Guidance-Chatbot.git

```

---

### 2️⃣ Create Virtual Environment

```bash
conda create -n emergencyfirstaidchatbot python=3.10 -y
```

---

### 3️⃣ Activate Virtual Environment (Windows)

```bash
conda activate emergencyfirstaidchatbot
```

---

### 4️⃣ Install Requirements

```bash
pip install -r requirements.txt
```

---

### 5️⃣ Pull Ollama Model

```bash
ollama pull phi
```

---

### 6️⃣ Set Pinecone API Key (Windows CMD)

```bash
set PINECONE_API_KEY=your_api_key
```

(If using PowerShell)

```powershell
$env:PINECONE_API_KEY="your_api_key"
```

---

### 7️⃣ Run the Application

```bash
python app.py
```

---

Open in browser:

```
http://127.0.0.1:5000
```

# Folder Structure

```markdown
## 📂 Project Structure

AI-Powered-Emergency-First-Aid-Guidance-Chatbot/
│
├── 📁 Data
│   └── First aid source documents (PDFs)
│
│
├── 📁 research
│   └── trials.ipynb  → RAG experimentation & testing
│
├── 📁 src
│   ├── __init__.py
│   ├── helper.py     → Embeddings, vector store, retriever setup
│   └── prompt.py     → Custom RAG prompt template
│
├── 📁 static
│   └── style.css     → Frontend styling
│
├── 📁 templates
│   └── index.html    → Chatbot UI (Frontend)
│
├── .env              → Environment variables (API keys)
├── .gitignore
├── app.py            → Flask backend + RAG pipeline integration
├── store_index.py    → Vector DB indexing script
├── setup.py          → Project configuration
├── requirements.txt  → Dependencies
├── LICENSE
└── README.md

## ⚠ Disclaimer

This application is for educational purposes only.  
It does NOT replace professional medical advice.  
In case of serious emergencies, contact medical professionals immediately.

## 🔮 Future Improvements

- Add conversation memory
- Add multilingual support
- Deploy using Docker
- Add user authentication
- Improve retrieval with re-ranking

