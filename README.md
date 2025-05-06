# 🤖 Imer-1.0 – Emotion-Aware AI Chatbot

![Hugging Face](https://img.shields.io/badge/Frontend-Hugging--Face-blue)
![Render](https://img.shields.io/badge/Backend-Render-green)
![Python](https://img.shields.io/badge/Python-3.10%2B-yellow)
![License](https://img.shields.io/badge/License-MIT-purple)

Welcome to **Imer-1.0**, an advanced emotion-aware AI chatbot that adapts to your mood and persona preferences. It supports **custom personalities**, intelligent memory, engaging GIF and quote suggestions, and more — all through a beautiful, animated Streamlit interface.

🌐 **Live Demo**: [Imer-1.0](https://ro08hi11t23-imer-1-0.hf.space)

---

## 📁 Project Structure

```
Imer-1.0/
├── frontend/
│   └── app.py                     # Streamlit-based UI
├── backend/
│   ├── app.py                     # FastAPI or Flask entry point for backend API
│   ├── __init__.py
│   ├── chatbot.py                 # Core chat logic and response formatting
│   ├── emotions.py                # Emotion detection module
│   ├── gifs.py                    # GIF suggestions based on context
│   ├── memory.py                  # Persistent memory using SQLite or JSON
│   ├── suggestions.py             # Quotes and music link generator
│   └── utils.py                   # Utility functions
├── requirements.txt
└── README.md
```

---

## 🧠 Features

### ✨ Dynamic Personalities
- 🤗 **Friendly** – Casual and comforting
- 😂 **Funny** – Witty and light-hearted
- 🧐 **Serious** – Professional tone

### 💬 Emotion-Aware Responses
- Auto-detects user emotion and tailors responses accordingly

### 🎵 Smart Suggestions
- Provides quotes, music, and GIFs based on mood/context

### 🧠 Memory Support
- Chat memory using SQLite or JSON for personalized conversation

### 🎨 Animated & Modern UI
- Sidebar with persona selector, animated GIFs, and contact links
- Inspired by network bar aesthetics

### 🔌 Seamless Backend Integration
- RESTful backend deployed separately on **Render**
- Frontend connects securely to API

---

## ⚙️ Tech Stack

- **Frontend**: Streamlit (deployed on Hugging Face Spaces)
- **Backend**: Python + FastAPI/Flask (deployed on Render)
- **Model**: Emotion classification, response generation (using Cohere/OpenAI)
- **Persistence**: SQLite or JSON-based memory

---

## 🚀 Setup Instructions

### ✅ Clone the Repo

```bash
git clone https://github.com/your-username/Imer-1.0.git
cd Imer-1.0
```

### 🧪 Backend Setup (Render Deployment)

1. Navigate to `backend/`
2. Create a `requirements.txt` file with dependencies
3. Deploy on [Render](https://render.com/) using a web service

Example `requirements.txt`:

```txt
fastapi
uvicorn
requests
openai
cohere
```
Start command:

```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```

### 🎨 Frontend Setup (Streamlit on Hugging Face)

1. Navigate to `frontend/`
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
streamlit run app.py
```

---

## 🛰️ Deployment

### Frontend
- Deployed on [Hugging Face Spaces](https://huggingface.co/spaces)
- URL: [Imer Frontend](https://ro08hi11t23-imer-1-0.hf.space)

### Backend
- Deploy `backend/app.py` on [Render](https://render.com/)
- Ensure public API endpoint is reachable by frontend

---

## 📬 Contact & Credits

Made with ❤️ by [Rohit Jena](https://github.com/RohitJena1075)

---

## 📄 License

This project is licensed under the MIT License.
