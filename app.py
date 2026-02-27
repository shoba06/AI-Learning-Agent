import streamlit as st
import joblib
import pandas as pd
import requests

st.set_page_config(page_title="AI Learning Agent", layout="centered")
st.title("🤖 Intelligent Personalized Learning Agent")

# =========================
# Load ML Model
# =========================
try:
    ml_model = joblib.load("model.pkl")
except:
    st.error("model.pkl not found! Run train_model.py first.")
    st.stop()

# =========================
# YouTube Video Fetch
# =========================
def get_youtube_video(topic):
    query = topic.replace(" ", "+") + "+tutorial"
    search_url = f"https://www.youtube.com/results?search_query={query}"

    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(search_url, headers=headers)

    for part in response.text.split('"'):
        if "watch?v=" in part:
            video_id = part.split("watch?v=")[-1][:11]
            return f"https://www.youtube.com/watch?v={video_id}"

    return None

# =========================
# User Inputs
# =========================
topic = st.text_input("📘 Enter the topic you want to learn:")

difficulty = st.selectbox(
    "🎯 Select Difficulty Level:",
    ["Beginner", "Intermediate", "Advanced"]
)

st.subheader("🧠 Answer your learning preferences:")

watches_videos = st.radio("Do you prefer watching videos?", ["Yes", "No"])
prefers_audio = st.radio("Do you prefer listening to lectures?", ["Yes", "No"])
likes_practical = st.radio("Do you enjoy practical activities?", ["Yes", "No"])
reads_notes = st.radio("Do you prefer reading notes?", ["Yes", "No"])

# =========================
# Generate Button
# =========================
if st.button("🚀 Generate Learning Content"):

    if topic.strip() == "":
        st.warning("Please enter a topic.")
        st.stop()

    input_data = pd.DataFrame([[
        1 if watches_videos == "Yes" else 0,
        1 if prefers_audio == "Yes" else 0,
        1 if likes_practical == "Yes" else 0,
        1 if reads_notes == "Yes" else 0
    ]], columns=[
        "watches_videos",
        "prefers_audio",
        "likes_practical",
        "reads_notes"
    ])

    style = ml_model.predict(input_data)[0]

    st.success(f"🎯 Detected Learning Style: {style}")

    # =========================
    # LLM Prompt
    # =========================
    prompt = f"""
    Explain {topic} in a detailed academic way.

    Difficulty Level: {difficulty}
    Learning Style: {style}

    Structure with:
    - Definition
    - Core Concepts
    - Example
    - Applications
    - Summary
    """

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    explanation = response.json()["response"]

    # =========================
    # Output
    # =========================
    st.header(f"📖 Learning Topic: {topic}")
    st.write(explanation)

    # =========================
    # Video (ONLY if Visual)
    # =========================
    if style.lower() == "visual" and watches_videos == "Yes":
        video_url = get_youtube_video(topic)
        if video_url:
            st.video(video_url)