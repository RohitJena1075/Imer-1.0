import streamlit as st
import requests
import random

WELCOME_GIFS = [
    "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExdXhmb3F4M29zbWFpcmptc3V0dmhlN2RydzJleGQ5bjE3M3p1d2c1ZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/1ZVBVvY5kS7qUHhqI2/giphy.gif",
    "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExY21wemt1aGNuOGsxN3NiMzM0NnQwY3FiZjgzaXU5cXR5MHQyODFyMiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Rsp9jLIy0VZOKlZziw/giphy.gif",
    "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExcXZsbXpjMHg2dmZpc21wbXFtdGtjMXgwZDNuZzFpdTN3YmV0N210MSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/XD9o33QG9BoMis7iM4/giphy.gif",
    "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExd21yamxsYTcxeWZpM29ocTE2cmd2c2l3bTgzb3hvYmI5cHhiNmd6NiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l0MYC0LajbaPoEADu/giphy.gif",
    "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExcWxvMGNzYTFhb3J1anJkcGUzaHVxdmFhNGs3N3FmNjR0MDFjcDV6ayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/n3jh2fO3GB4aaK6tAd/giphy.gif",
    "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExMHN4cTByeTZhNWpqeXh2cWc3d2E3MnZ5NnoyZXpoZWRkMmZtOHpuNiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l4JyOCNEfXvVYEqB2/giphy.gif",
    "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExbWM2ajF2MXU5NnEwOWhmMnB5azhxMnlybm16ZWp1aHEyOW5vMTQ3MiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ggtpYV17RP9lTbc542/giphy.gif"
]


# 🎨 Streamlit Page Configuration
st.set_page_config(page_title="AI Companion", layout="centered")
st.markdown("""
    <style>
    /* Increase avatar size */
    [data-testid="chat-message-avatar"] img {
        height: 70px !important;
        width: 70px !important;
        object-fit: cover;
        border-radius: 50%;
    }

    /* Style assistant message block */
    [data-testid="chat-message"] div:has(img[src*="S60CrN9iMxFlyp7uM8"]) {
        background-color: #e0f7ff;
        padding: 30px 25px !important;
        border-radius: 20px;
        font-size: 1.2rem;
        line-height: 1.6;
        margin-bottom: 10px;
        box-shadow: 0px 2px 8px rgba(0, 0, 0, 0.05);
    }

    /* Style user message block */
    [data-testid="chat-message"] div:has(img[src*="wlHIxNluDY02O4x3a4"]) {
        font-size: 1.1rem;
        line-height: 1.5;
        padding: 25px !important;
    }
    </style>
""", unsafe_allow_html=True)



# 🧠 Backend API URL
API_URL = "https://imer-1-0.onrender.com/chat"

# 🧾 Session History
if "history" not in st.session_state:
    st.session_state["history"] = []

# 🎭 Sidebar - Cool UI
with st.sidebar:
    st.image("https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExZXZxcnVlNG52aXIwNjhzYTI3Z3YwdzI1azg4dXdxNDZibDgwcGdsdSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/S60CrN9iMxFlyp7uM8/giphy.gif", caption="Imer-1.0", use_container_width=True)
    st.header("🧠 Bot Personality")
    personality = st.radio("Choose one:", ["🤗 Friendly", "😂 Funny", "🧐 Serious"], index=0)

    st.markdown("""
    <hr><p style='font-size: 14px; color: #555;'>Choose your AI persona!<br>- Friendly: Feel the warmth of a cozy chat.<br>- Funny: Let the banter begin!<br>- Serious: Straight to business, no fluff.</p><hr>
    <small>✨ Created with ❤️ by ro08hi11t23</small>
    """, unsafe_allow_html=True)

# 💬 Chat Input
user_input = st.chat_input("Type something to your AI friend...")

# 🚀 Handle API Call
if user_input:
    with st.spinner("🤖 Thinking..."):
        try:
            res = requests.post(API_URL, json={
                "message": user_input,
                "personality": personality.strip("🧐😂🤗 ")
            }).json()

            if "error" in res:
                st.error(f"❌ Backend Error: {res['error']}")
            else:
                st.session_state["history"].append({
                    "user": user_input,
                    "bot": res["reply"],
                    "emotion": res["emotion"],
                    "gif": res["gif"],
                    "quote": res["quote"],
                    "music": res["music"]
                })
        except Exception as e:
            st.error(f"🚫 Failed to connect to backend: {e}")


# 👋 Initial Welcome Message if no chat yet
if not st.session_state["history"]:
    welcome_gif = random.choice(WELCOME_GIFS)
    st.markdown("## 👋 Welcome to your AI Companion!")
    st.markdown("Start chatting to see how I react to your emotions. 🎭")
    st.image(welcome_gif, use_container_width=True)
    st.markdown("""
        <div style='text-align: center; font-size: 16px; color: grey;'>
        Try saying something like:<br>
        <i>"I'm feeling down today..."</i> or <i>"Tell me a joke!"</i>
        </div>
    """, unsafe_allow_html=True)

# 🧾 Chat History Display
for msg in st.session_state["history"]:
    with st.chat_message("user", avatar="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExcTNsZDV5NWh1ajM2d3R3OW45bHJkc3llaDl6NWFoMXd5MHBiYXM3byZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/wlHIxNluDY02O4x3a4/giphy.gif"):
        st.markdown(msg["user"])

    with st.chat_message("assistant", avatar="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExZXZxcnVlNG52aXIwNjhzYTI3Z3YwdzI1azg4dXdxNDZibDgwcGdsdSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/S60CrN9iMxFlyp7uM8/giphy.gif"):
        st.markdown(f"`Emotion: {msg['emotion']}`\n\n{msg['bot']}")

        with st.expander("🎞️ Reaction GIF"):
            st.image(msg["gif"], use_container_width=True)

        st.markdown(f"🎵 [**Vibe with Music** ]({msg['music']})", unsafe_allow_html=True)
        st.success(f"💡 {msg['quote']}")



