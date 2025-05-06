import os
os.environ["HOME"] = "/tmp"  # Make ~/.streamlit writable

import streamlit as st
import requests
import random
from datetime import datetime

# Backend API
API_URL = "https://imer-1-0.onrender.com/chat"

# Welcome GIFs
WELCOME_GIFS = [
    "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExdXhmb3F4M29zbWFpcmptc3V0dmhlN2RydzJleGQ5bjE3M3p1d2c1ZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/1ZVBVvY5kS7qUHhqI2/giphy.gif",
    "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExY21wemt1aGNuOGsxN3NiMzM0NnQwY3FiZjgzaXU5cXR5MHQyODFyMiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Rsp9jLIy0VZOKlZziw/giphy.gif",
    "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExcXZsbXpjMHg2dmZpc21wbXFtdGtjMXgwZDNuZzFpdTN3YmV0N210MSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/XD9o33QG9BoMis7iM4/giphy.gif"
]

# Page config
st.set_page_config(page_title="AI Companion", layout="wide")

# Inject CSS for sidebar styling and smooth connect box
st.markdown("""
    <style>
    [data-testid="stSidebar"] {
        background-color: #1e1e2f;
        padding: 25px;
    }
    .persona-section {
        background: #2c2c3f;
        padding: 20px;
        border-radius: 10px;
        margin-top: 20px;
    }
    .persona-section h4 {
        text-align: center;
        color: #f4f4f4;
        font-size: 18px;
        margin-bottom: 10px;
    }
    .persona-section p {
        color: #ccc;
        font-size: 13px;
        line-height: 1.5;
        margin-left: 8px;
    }
    .connect-links {
        background-color: #33384e;
        border-radius: 10px;
        padding: 10px 15px;
        margin-top: 10px;
        font-size: 15px;
        color: white;
    }
    .connect-links a {
        color: #91e0ff;
        text-decoration: none;
    }
    </style>
""", unsafe_allow_html=True)

# Session
if "history" not in st.session_state:
    st.session_state["history"] = []
if "show_connect" not in st.session_state:
    st.session_state["show_connect"] = False

# Sidebar
with st.sidebar:
    st.image("https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExZXZxcnVlNG52aXIwNjhzYTI3Z3YwdzI1azg4dXdxNDZibDgwcGdsdSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/S60CrN9iMxFlyp7uM8/giphy.gif", use_container_width=True)
    st.markdown("<h3 style='text-align: center; color: white;'>Imer-1.0</h3>", unsafe_allow_html=True)

    with st.container():
        st.markdown("""
        <div class='persona-section'>
            <h4>🧠 Choose your AI Persona</h4>
            <p>🤗 <b>Friendly</b> – A cozy and warm chat.<br>
            😂 <b>Funny</b> – Banter and jokes coming your way!<br>
            🧐 <b>Serious</b> – Straight talk, no nonsense.</p>
        </div>
        """, unsafe_allow_html=True)
        personality = st.radio("", ["🤗 Friendly", "😂 Funny", "🧐 Serious"], index=0)

    if st.button("🗑️ Clear Chat"):
        st.session_state["history"] = []
        try:
            st.rerun()
        except:
            pass

    st.markdown("<br>", unsafe_allow_html=True)  # Space between buttons

    if st.button("🌐 Connect With Me"):
        st.session_state["show_connect"] = not st.session_state["show_connect"]

    if st.session_state["show_connect"]:
        st.markdown("""
        <div class="connect-links">
            <a href="https://github.com/RohitJena1075" target="_blank">🐙 GitHub</a><br>
            <a href="https://www.linkedin.com/in/rohitjena2526" target="_blank">💼 LinkedIn</a><br>
            📧 rohit.jena2004@gmail.com
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <hr><p style='font-size: 14px; color: #ccc;'>✨ Created with ❤️ by ro08hi11t23</p>
    """, unsafe_allow_html=True)

# Chat input
user_input = st.chat_input("Type something to your AI friend...")

# Handle API Call
if user_input and user_input.strip():
    with st.spinner("🤖 Evaluating your thoughts..."):
        try:
            response = requests.post(API_URL, json={
                "message": user_input,
                "personality": personality.replace("🤗 ", "").replace("😂 ", "").replace("🧐 ", "")
            })
            if response.status_code == 200:
                data = response.json()
                st.session_state["history"].append({
                    "user": user_input,
                    "bot": data.get("reply", "Hmm... I’m not sure how to respond."),
                    "emotion": data.get("emotion", "neutral"),
                    "gif": data.get("gif", ""),
                    "quote": data.get("quote", ""),
                    "music": data.get("music", ""),
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "persona_icon": personality.split(" ")[0]
                })
            else:
                st.error(f"Backend error: {response.text}")
        except Exception as e:
            st.error(f"Connection failed: {e}")

# Initial welcome message
if not st.session_state["history"]:
    st.markdown("## 👋 Welcome to Folks I am Imer!")
    st.markdown("Start chatting to see how I react to your emotions. 🎭")
    st.image(random.choice(WELCOME_GIFS), use_container_width=True)
    st.markdown("""
        <div style='text-align: center; font-size: 16px; color: grey;'>
        Try saying something like:<br>
        <i>"I'm feeling down today..."</i> or <i>"Tell me a joke!"</i>
        </div>
    """, unsafe_allow_html=True)

# Chat history
for msg in st.session_state["history"]:
    with st.chat_message("user", avatar="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExcTNsZDV5NWh1ajM2d3R3OW45bHJkc3llaDl6NWFoMXd5MHBiYXM3byZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/wlHIxNluDY02O4x3a4/giphy.gif"):
        st.markdown(msg["user"])
        st.caption(f"🕒 {msg['timestamp']}")

    with st.chat_message("assistant", avatar="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExZXZxcnVlNG52aXIwNjhzYTI3Z3YwdzI1azg4dXdxNDZibDgwcGdsdSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/S60CrN9iMxFlyp7uM8/giphy.gif"):
        st.markdown(f"`{msg['persona_icon']} Emotion: {msg['emotion']}`\n\n{msg['bot']}")
        st.caption(f"🕒 {msg['timestamp']}")
        if msg["gif"]:
            with st.expander("🎞️ Reaction GIF"):
                st.image(msg["gif"], use_container_width=True)
        if msg["music"]:
            st.markdown(f"🎧 <b>Feeling the vibe?</b> <a href='{msg['music']}' target='_blank'>Click here to listen!</a>", unsafe_allow_html=True)
        if msg["quote"]:
            st.success(f"💡 {msg['quote']}")
