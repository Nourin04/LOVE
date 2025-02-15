import streamlit as st
import random
import os
import requests
from textblob import TextBlob
from transformers import AutoTokenizer

# Get Hugging Face API key from environment variable
API_KEY = os.getenv("HUGGINGFACE_API_KEY")

# Function: Generate AI Love Story using Hugging Face API
def generate_ai_love_story(names, place, event, memory):
    api_key = st.secrets["HUGGINGFACE_TOKEN"]  # Fetch API key from Streamlit secrets
    api_url = "https://api-inference.huggingface.co/models/tiiuae/falcon-7b-instruct"

    headers = {"Authorization": f"Bearer {api_key}"}
    prompt = (f"Write a heartfelt, emotional, and magical love story about {names}. "
              f"They met at {place}, a place full of memories that changed their lives forever. "
              f"Describe the atmosphere and feelings they experienced when they first met. "
              f"A memorable moment they cherish together is {memory}, and this memory always brings them closer. "
              f"One event that deepened their love was {event}, where they truly understood how much they meant to each other. "
              f"Include moments of tension, excitement, and love, making it a truly enchanting and unforgettable story. "
              f"Make the love story vivid, passionate, and real.")

    payload = {
        "inputs": prompt, 
        "parameters": {
            "max_length": 500, 
            "temperature": 0.7, 
            "top_k": 50
        }
    }

    try:
        response = requests.post(api_url, headers=headers, json=payload, timeout=10)
        response.raise_for_status()  # Raise error for non-2xx status codes
        story = response.json()[0]["generated_text"]
        return story
    except requests.exceptions.Timeout:
        return "Error: Request timed out. Please try again later."
    except requests.exceptions.RequestException as e:
        return f"Error: An issue occurred while contacting the model ({str(e)})."
    except (KeyError, IndexError):
        return "Error: Unexpected response format from the AI model."


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
    "A simple 'I love you' can make all the difference. 💖",
    "Support each other's dreams and ambitions. Together, you're unstoppable! 🌟",
    "Love is patient, love is kind—never forget the little things that matter. 💫",
    "Appreciate your partner for the unique person they are. ✨",
    "Sometimes the best way to show love is through listening. 👂💬",
    "Create memories together that will last a lifetime. 📸",
    "Give your partner the space to grow while remaining their biggest supporter. 🌱",
    "Cherish the quiet moments, they are just as precious as the loud ones. 💕",
    "Laughter is the best glue to hold a relationship together. 😂",
    "Compromise is the key to a happy relationship—meet each other halfway. 🤝",
    "Sometimes, the best thing you can do for your relationship is to simply be present. 🕰️",
    "Forgiveness is a powerful act of love—don’t hold onto grudges. 💞",
    "A healthy relationship thrives on honesty, trust, and mutual respect. 🔑",
    "Don’t be afraid to express your feelings, vulnerability is a strength. 💪💌",
    "Love is not just a feeling, it's an action you show every day. 💘",
    "Go on adventures together, and create memories that make your bond unbreakable. 🌍"
]

    return random.choice(advice_list)

# Function: Mini Games for Couples
def get_love_game():
    questions = [
    "Would you rather go on a romantic beach date or a cozy movie night? 🍿🏖️",
    "Would you rather receive love letters or surprise gifts? 💌🎁",
    "Would you rather cook together or dance together? 🍽️💃",
    "Would you rather have breakfast in bed or a candlelight dinner? 🍳🕯️",
    "Would you rather have a picnic in the park or stargazing on the roof? 🧺🌌",
    "Would you rather go on a spontaneous road trip or have a planned romantic getaway? 🚗✈️",
    "Would you rather watch the sunset together or watch the sunrise? 🌅🌄",
    "Would you rather cuddle on the couch or take a walk hand-in-hand? 🛋️🚶‍♀️",
    "Would you rather receive a handwritten poem or a love song written just for you? ✍️🎶",
    "Would you rather take a dance class together or try cooking a new recipe? 💃🍝",
    "Would you rather spend a day at the spa or a day hiking in nature? 💆‍♀️🏞️",
    "Would you rather have a quiet night in or go out for a night of fun? 🏠🎉",
    "Would you rather surprise your partner with a thoughtful gesture or a romantic date night? 🎁🌹",
    "Would you rather have a long-distance relationship or a close relationship with everyday moments? 📱💑",
    "Would you rather make each other breakfast every Sunday or dinner every Friday? 🍳🍴",
    "Would you rather travel to a country you've both never been to or revisit a place you both love? 🌍✈️",
    "Would you rather share a passionate kiss under the rain or on top of a mountain? 💋⛰️",
    "Would you rather spend a day volunteering together or take a weekend trip to explore a new city? 🌍🤝"
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
    "Plan a surprise date—could be a movie night or a simple walk! 🎬🌙",
    "Compliment your partner on something you admire about them today. 🌟💬",
    "Surprise them with their favorite dessert after dinner. 🍰🍓",
    "Give your partner a heartfelt hug and tell them how much they mean to you. 🤗💘",
    "Create a playlist of songs that remind you of your relationship and share it with them. 🎶💑",
    "Leave a sweet message on their mirror for them to find later. ✨💋",
    "Take a selfie together and make it your phone wallpaper. 📸💖",
    "Plan a mini adventure for the weekend—something spontaneous and fun! 🗺️🎉",
    "Share a memory from your past that made you fall in love with them. 🧡📖",
    "Write a short poem about your relationship and share it with them. ✍️💞",
    "Take a break from technology and spend uninterrupted quality time together. 📵💑",
    "Create a small surprise for them to find during the day—a favorite snack, a handwritten note, etc. 🎁❤️",
    "Give them a little DIY gift that shows how much you care. 🎨💝",
    "Remind them of a funny memory you both cherish and laugh together. 😂💖",
    "Do something they enjoy, even if it’s not your favorite activity—showing support. 🎮❤️"
]

    return random.choice(challenges)

# Sidebar: Display Chatbot
st.sidebar.header("Love Chatbot 🤖")
user_input = st.sidebar.text_input("Chat with the Love Chatbot...", key="sidebar_chatbot_input")
if st.sidebar.button("Send Message 💬", key="sidebar_chatbot_btn"):
    if user_input:
        response = chatbot_response(user_input)
        st.sidebar.success(f"Chatbot: {response}")
    else:
        st.sidebar.warning("Please type a message to start the conversation.")

# Main Layout: Tabs
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs([
    "Love Score 💕", "Love Advice 💌", "Mini Games 🎮", 
    "Love Story 📖", "Chat Analysis 💬", 
    "Zodiac Match ✨", "Love Challenge 🎯", "Love Chatbot 🤖"
])

# ---- Tab 1: Love Score ----
with tab1:
    st.header("💖 Love Score Calculator 💖")
    name1 = st.text_input("Enter your name", key="name1")
    name2 = st.text_input("Enter your partner's name", key="name2")
    birth1 = st.text_input("Enter your birth date (YYYY-MM-DD)", key="birth1")
    birth2 = st.text_input("Enter your partner's birth date (YYYY-MM-DD)", key="birth2")
    if st.button("Calculate Love Score 💕"):
        if name1 and name2 and birth1 and birth2:
            result = calculate_love(name1, name2, birth1, birth2)
            st.success(result)
        else:
            st.warning("Please fill in all fields!")

# ---- Tab 2: Love Advice ----
with tab2:
    st.header("💌 Love Advice 💌")
    st.write(get_love_advice())

# ---- Tab 3: Mini Games ----
with tab3:
    st.header("🎮 Mini Games for Couples 🎮")
    st.write(get_love_game())

# ---- Tab 4: Love Story ----
with tab4:
    st.header("📖 AI Love Story 📖")
    names = st.text_input("Enter names of the couple", key="names")
    place = st.text_input("Enter the place where they met", key="place")
    event = st.text_input("Enter a memorable event they shared", key="event")
    memory = st.text_input("Enter a cherished memory", key="memory")
    if st.button("Generate Love Story 💖"):
        if names and place and event and memory:
            story = generate_ai_love_story(names, place, event, memory)
            st.success(story)
        else:
            st.warning("Please fill in all fields!")

# ---- Tab 5: Chat Analysis ----
with tab5:
    st.header("💬 Chat Sentiment Analysis 💬")
    chat_text = st.text_area("Enter your chat text", key="chat_text")
    if st.button("Analyze Sentiment 📊"):
        if chat_text:
            sentiment = analyze_chat(chat_text)
            st.success(sentiment)
        else:
            st.warning("Please enter chat text to analyze!")

# ---- Tab 6: Zodiac Match ----
with tab6:
    st.header("✨ Zodiac Match ✨")
    zodiac1 = st.text_input("Enter your zodiac sign", key="zodiac1")
    zodiac2 = st.text_input("Enter your partner's zodiac sign", key="zodiac2")
    if st.button("Check Compatibility 💫"):
        if zodiac1 and zodiac2:
            match = zodiac_match(zodiac1, zodiac2)
            st.success(match)
        else:
            st.warning("Please enter both zodiac signs!")

# ---- Tab 7: Daily Love Challenge ----
with tab7:
    st.header("🎯 Daily Love Challenge 🎯")
    st.write(daily_love_challenge())
