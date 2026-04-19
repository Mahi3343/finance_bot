# 📊 Finance AI Tutor Bot

An interactive AI-driven educational bot for the **Finance domain** that helps users learn from uploaded reports through quizzes, answer evaluation, and personalized explanations.

This project uses **FastAPI + Streamlit + Groq LLM + Vector DB Ready Architecture**.

---

# 🚀 Features

* 📄 Upload PDF Finance Reports
* 🧠 AI Quiz Generation from uploaded documents
* ✅ Automatic Answer Evaluation
* 💡 Detailed Explanations for Wrong Answers
* 🎯 Personalized Learning Experience
* 🌐 Interactive Streamlit Frontend
* ⚡ FastAPI Backend APIs
* 🗂 Vector Database Ready (RAG Upgrade)

---

# 🛠 Tech Stack

## Backend

* Python
* FastAPI
* Uvicorn

## Frontend

* Streamlit

## AI / LLM

* Groq API

## PDF Reader

* PyMuPDF

## Optional Future Upgrade

* ChromaDB
* LangChain

---

# 📁 Project Structure

```text
finance-ai-bot/
│── backend/
│   │── main.py
│   │── llm.py
│   │── quiz_engine.py
│   │── evaluation_engine.py
│   │── pdf_reader.py
│   │── vector_store.py
│   │── requirements.txt
│   │── .env
│   └── venv/
│
│── frontend/
│   └── app.py
│
└── README.md
```

---

# ⚙️ Installation Guide

## 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/finance-ai-bot.git
cd finance-ai-bot
```

---

# 2️⃣ Setup Backend

```bash
cd backend
python -m venv venv
```

## Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

---

# 3️⃣ Install Dependencies

```bash
python -m pip install -r requirements.txt
```

If requirements file not available:

```bash
python -m pip install fastapi uvicorn python-multipart groq python-dotenv pymupdf streamlit requests chromadb sentence-transformers
```

---

# 4️⃣ Environment Variables

Create file:

```text
backend/.env
```

Add:

```env
GROQ_API_KEY=your_groq_api_key_here
```

---

# 🚀 Run Backend

Inside `backend/`

```bash
uvicorn main:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

Swagger Docs:

```text
http://127.0.0.1:8000/docs
```

---

# 🌐 Run Frontend

Open new terminal:

```bash
cd frontend
python -m streamlit run app.py
```

Frontend URL:

```text
http://localhost:8501
```

---

# 📌 Available APIs

## GET /

Health Check

---

## POST /upload-report

Upload PDF and generate AI quiz.

---

## POST /evaluate-answer

Evaluate selected answer and return explanation.

---

## POST /ask-report

Search uploaded report using Vector DB.

---

# 🧪 Example Workflow

1. Run backend server
2. Run frontend app
3. Upload PDF report
4. Generate quiz
5. Select answers
6. Get explanations
7. Learn finance concepts interactively

---

# 🔐 Important Notes

* Never upload `.env` to GitHub
* Add `.env` in `.gitignore`
* Keep API keys private

---

# 📄 Example `.gitignore`

```text
venv/
.env
__pycache__/
*.pyc
chroma_db/
```

---

# 🚀 Future Enhancements

* 📊 Analytics Dashboard
* 👤 User Login System
* 🧠 Adaptive Learning Paths
* ☁ Cloud Deployment
* 📈 Real Financial Report Analysis
* 🔍 Full RAG Assistant

---

# 👨‍💻 Author

Finance AI Tutor Bot Project

---
