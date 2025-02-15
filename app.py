import streamlit as st
import random
import requests
import cv2
import numpy as np
from textblob import TextBlob
import datetime

# Function: Love Compatibility Score (Using Names & Birth Dates)
def calculate_love(name1, name2, birth1, birth2):
    random.seed(name1 + name2 + birth1 + birth2)  # Seed based on user input
    score = random.randint(50, 100)
    return f"💖 {name1} and {name2} have a love compatibility of {score}%! 💖"

# Function: AI Love Advice Chatbot (Pre-trained Love Quotes & Advice)
def get_love_advice():
    advice_list = [
        "True love is about growing together. Keep supporting each other! ❤️",
        "Trust, communication, and fun—these make love last forever! 💕",
        "Surprise your partner today with a small, meaningful gesture. 🌹",
        "Never stop dating your partner, even after years together! 🎉",
        "Love is about patience and understanding—keep learning about each other. 😊"
    ]
    return random.choice(advice_list)

# Function: Mini Games for Couples
def get_love_game():
    questions = [
        "Would you rather go on a romantic beach date or a cozy movie night? 🍿🏖️",
        "Would you rather receive love letters or surprise gifts? 💌🎁",
        "Would you rather cook together or dance together? 🍽️💃",
        "Would you rather relive your first date or create a new surprise date? 💞"
    ]
    return random.choice(questions)

# Function: Love Story Generator
def generate_love_story(name1, name2):
    story_templates = [
        f"Once upon a time, {name1} met {name2} under the shining moonlight. Their eyes met, and it was love at first sight. From that day on, they embarked on a journey of love and laughter, creating beautiful memories together. 💖",
        f"{name1} and {name2} were childhood friends who lost touch. Years later, fate brought them back together at a coffee shop. The moment they saw each other, they knew—this was destiny! ☕💘",
        f"A romantic road trip turned into an unforgettable love story when {name1} and {name2} got lost in a small town, discovering hidden gems and each other’s deepest secrets. 🚗💞"
    ]
    return random.choice(story_templates)

# Function: Photo Compatibility Analysis (Mockup - Placeholder)
def analyze_photo(image):
    return "AI thinks your smiles match perfectly! 😊💑 (Feature coming soon)"

# Function: Text Sentiment Analysis
def analyze_chat(chat_text):
    blob = TextBlob(chat_text)
    sentiment = blob.sentiment.polarity
    if sentiment > 0.2:
        return "Your messages are filled with love and positivity! ❤️"
    elif sentiment < -0.2:
        return "Your chats need more love and kindness! 💔"
    else:
        return "Your messages are neutral! 💬"

# Function: Zodiac & Numerology Match
def zodiac_match(zodiac1, zodiac2):
    compatible_pairs = [
        ("Aries", "Leo"), ("Taurus", "Virgo"), ("Gemini", "Libra"),
        ("Cancer", "Pisces"), ("Leo", "Sagittarius"), ("Virgo", "Capricorn"),
        ("Libra", "Aquarius"), ("Scorpio", "Cancer"), ("Sagittarius", "Aries"),
        ("Capricorn", "Taurus"), ("Aquarius", "Gemini"), ("Pisces", "Scorpio")
    ]
    if (zodiac1, zodiac2) in compatible_pairs or (zodiac2, zodiac1) in compatible_pairs:
        return f"💘 {zodiac1} and {zodiac2} are highly compatible!"
    else:
        return f"🤔 {zodiac1} and {zodiac2} may need more effort in love."

# Function: Daily Love Challenge
def daily_love_challenge():
    challenges = [
        "Send your partner a cute voice note today. 🎙️💌",
        "Write a small love note and hide it in their bag. 📝💖",
        "Cook their favorite dish for dinner tonight. 🍽️💞",
        "Plan a surprise date—could be a movie night or a simple walk! 🎬🌙",
        "Tell them 3 things you love about them. 💕"
    ]
    return random.choice(challenges)

# Streamlit Web App
st.title("💖 AI Love Calculator & Fun Games 💖")

# Input Fields
name1 = st.text_input("Enter Your Name:")
birth1 = st.text_input("Enter Your Birth Date (YYYY-MM-DD):")
name2 = st.text_input("Enter Partner's Name:")
birth2 = st.text_input("Enter Partner's Birth Date (YYYY-MM-DD):")

if st.button("Calculate Love Score 💕"):
    result = calculate_love(name1, name2, birth1, birth2)
    st.success(result)

# AI Love Advice Chatbot
st.subheader("💌 AI Love Advice")
if st.button("Get Love Advice 💬"):
    advice = get_love_advice()
    st.info(advice)

# Mini Games for Couples
st.subheader("🎮 Love Game Time!")
if st.button("Get a Fun Love Question 🎲"):
    question = get_love_game()
    st.warning(question)

# Love Story Generator
st.subheader("📖 AI Love Story Generator")
if st.button("Generate a Love Story ❤️"):
    story = generate_love_story(name1, name2)
    st.success(story)

# Photo Compatibility (Mockup)
st.subheader("📷 AI Photo Compatibility Analysis")
uploaded_file = st.file_uploader("Upload a couple's photo", type=["jpg", "png"])
if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    st.success(analyze_photo(uploaded_file))

# Chat Sentiment Analysis
st.subheader("💬 Chat Sentiment Check")
chat_text = st.text_area("Paste your recent chat messages here:")
if st.button("Analyze Chat 💌"):
    sentiment_result = analyze_chat(chat_text)
    st.warning(sentiment_result)

# Zodiac Compatibility
st.subheader("✨ Zodiac Love Match")
zodiac1 = st.selectbox("Your Zodiac Sign:", ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"])
zodiac2 = st.selectbox("Partner's Zodiac Sign:", ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"])
if st.button("Check Zodiac Compatibility 🌟"):
    st.success(zodiac_match(zodiac1, zodiac2))

# Daily Love Challenge
st.subheader("💖 Love Challenge of the Day")
if st.button("Get Today's Challenge 🎯"):
    st.info(daily_love_challenge())
