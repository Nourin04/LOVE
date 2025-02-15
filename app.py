import streamlit as st
import random
import os
import requests
from textblob import TextBlob

# Get Hugging Face API key from environment variable
API_KEY = os.getenv("HUGGINGFACE_API_KEY")

# Function: Generate AI Love Story using Hugging Face API
def generate_ai_love_story(names, place, event, memory):
    api_key = st.secrets["HUGGINGFACE_TOKEN"]  # Fetch API key from Streamlit secrets
    
    tokenizer = AutoTokenizer.from_pretrained("facebook/opt-1.3b", use_auth_token=api_key)
    model = AutoModelForCausalLM.from_pretrained("facebook/opt-1.3b", use_auth_token=api_key)

    prompt = (f"Write a romantic love story about {names}. "
              f"They met at {place}, and their most memorable moment was {memory}. "
              f"The event that brought them closer was {event}. "
              f"Make the story emotional, heartwarming, and magical.")

    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs, max_length=250, temperature=0.7, do_sample=True)
    story = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return story

# Function: Love Compatibility Score
def calculate_love(name1, name2, birth1, birth2):
    random.seed(name1 + name2 + birth1 + birth2)  
    score = random.randint(50, 100)
    return f"\U0001F496 {name1} and {name2} have a love compatibility of {score}%! \U0001F496"

# Function: AI Love Advice Chatbot
def get_love_advice():
    advice_list = [
        "True love is about growing together. ❤️",
        "Trust, communication, and fun—make love last forever! 💕",
        "Surprise your partner with a small, meaningful gesture today. 🌹",
        "Never stop dating your partner, even after years together! 🎉",
    ]
    return random.choice(advice_list)

# Function: Mini Games for Couples
def get_love_game():
    questions = [
        "Would you rather go on a romantic beach date or a cozy movie night? 🍿🏖️",
        "Would you rather receive love letters or surprise gifts? 💌🎁",
        "Would you rather cook together or dance together? 🍽️💃"
    ]
    return random.choice(questions)

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

# Function: Zodiac Compatibility
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
        "Plan a surprise date—could be a movie night or a simple walk! 🎬🌙"
    ]
    return random.choice(challenges)

# Streamlit Web App
st.title("💖 AI Love Calculator & Fun Games 💖")

# Create Tabs
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
    "Love Score 💕", "Love Advice 💌", "Mini Games 🎮", 
    "Love Story 📖", "Chat Analysis 💬", 
    "Zodiac Match ✨", "Love Challenge 🎯"
])

# ---- TAB 1: Love Compatibility Score ----
with tab1:
    st.header("💞 Love Compatibility Score")
    name1 = st.text_input("Enter Your Name:")
    birth1 = st.text_input("Enter Your Birth Date (YYYY-MM-DD):")
    name2 = st.text_input("Enter Partner's Name:")
    birth2 = st.text_input("Enter Partner's Birth Date (YYYY-MM-DD):")
    
    if st.button("Calculate Love Score 💕"):
        result = calculate_love(name1, name2, birth1, birth2)
        st.success(result)

# ---- TAB 2: AI Love Advice Chatbot ----
with tab2:
    st.header("💌 AI Love Advice")
    if st.button("Get Love Advice 💬"):
        advice = get_love_advice()
        st.info(advice)

# ---- TAB 3: Mini Games for Couples ----
with tab3:
    st.header("🎮 Love Game Time!")
    if st.button("Get a Fun Love Question 🎲"):
        question = get_love_game()
        st.warning(question)

# ---- TAB 4: Love Story Generator ----
with tab4:
    st.header("📖 AI Love Story Generator")
    place = st.text_input("Where did you meet?")
    event = st.text_input("A special event in your relationship:")
    memory = st.text_input("A favorite shared memory:")
    
    if st.button("Generate My Love Story ❤️"):
        if name1 and name2 and place and event and memory:
            story = generate_ai_love_story(f"{name1} and {name2}", place, event, memory)
            st.success(story)
        else:
            st.warning("Please fill in all fields to generate your love story.")

# ---- TAB 5: Chat Sentiment Analysis ----
with tab5:
    st.header("💬 Chat Sentiment Check")
    chat_text = st.text_area("Paste your recent chat messages here:")
    if st.button("Analyze Chat 💌"):
        sentiment_result = analyze_chat(chat_text)
        st.warning(sentiment_result)

# ---- TAB 6: Zodiac Compatibility ----
with tab6:
    st.header("✨ Zodiac Love Match")
    zodiac1 = st.selectbox("Select Your Zodiac Sign", ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"])
    zodiac2 = st.selectbox("Select Partner's Zodiac Sign", ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"])
    if st.button("Check Zodiac Compatibility 🌟"):
        st.success(zodiac_match(zodiac1, zodiac2))

# ---- TAB 7: Daily Love Challenge ----
with tab7:
    st.header("💖 Love Challenge of the Day")
    if st.button("Get Today's Challenge 🎯"):
        st.info(daily_love_challenge())
