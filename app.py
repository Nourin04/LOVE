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
            "max_length": 200, 
            "temperature": 0.5, 
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

# Streamlit Web App
st.title("💖✨  HeartTales : Where Love Stories Begin ✨💖")
st.markdown("#### *Every love story deserves to be told.*")

# Set the background image URL (local or from the web)
from PIL import Image

# Path to the image in your repo
background_image_url = "https://www.vecteezy.com/photo/53211687-a-red-felt-heart-surrounded-by-white-decorative-hearts-with-a-soft-bokeh-background-for-romance"  # Adjust this if the image is in a different folder

st.markdown(
    f"""
    <style>
    body {{
        background-image: url({background_image_url});
        background-size: cover;  /* Stretch the image to cover full size */
        background-position: center center;  /* Center the image */
        background-repeat: no-repeat;  /* Prevent repetition */
        min-height: 100vh;  /* Ensure full height of the screen */
        margin: 0;
        padding: 0;
        background-color: rgba(0, 0, 0, 0.5);  /* Apply semi-transparent dark overlay */
    }}
    .stApp {{
        background: transparent;
    }}
    .stContainer {{
        background: rgba(255, 255, 255, 0.8);  /* Apply semi-transparent white background to containers */
        border-radius: 10px;
        padding: 15px;
    }}
    h1, h2, h3, h4, h5, h6 {{
        font-weight: bold !important;
        
    }}
    .stButton {{
    /* Button background color */
        font-weight: bold;
    }}
    </style>
    """, 
    unsafe_allow_html=True
)

# Create Tabs
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9 = st.tabs([
    "Love Score 💕", "Personality Test-Based Compatibility 🧠", "Love Advice 💌", "Mini Games 🎮", "Love Story Compatibility 💖", 
    "Love Story Generator📖", "Chat Analysis 💬", 
    "Zodiac Match ✨", "Love Challenge 🎯"
])

# ---- TAB 1: Love Compatibility Score ----
with tab1:
    st.header("💞 Love Compatibility Score")
    name1 = st.text_input("Enter Your Name:", key="love_name1")
    birth1 = st.text_input("Enter Your Birth Date (YYYY-MM-DD):", key="love_birth1")
    name2 = st.text_input("Enter Partner's Name:", key="love_name2")
    birth2 = st.text_input("Enter Partner's Birth Date (YYYY-MM-DD):", key="love_birth2")
    
    if st.button("Calculate Love Score 💕", key="love_score_btn"):
        result = calculate_love(name1, name2, birth1, birth2)
        st.success(result)


# ---- TAB 2: Personality Test-Based Love Compatibility ----
with tab2:
    st.header("💖 Personality Test-Based Love Compatibility")
    st.markdown(
        """
        Take this quick personality test to see how well you and your partner match!
        Answer the following questions based on your preferences:
        """
    )

    # Define personality test questions
    questions = [
        ("How do you feel about spontaneous adventures?", ["Love it!", "Not for me"]),
        ("What’s your ideal weekend activity?", ["Relaxing at home", "Exploring new places"]),
        ("How do you handle disagreements?", ["I prefer to talk it out", "I like to have some space"]),
        ("How do you express love?", ["Through words", "Through actions"]),
        ("What’s your idea of a perfect date?", ["Romantic dinner", "Fun outdoor activity"]),
    ]
    
    # Collect answers for "Him"
    st.subheader("His Answers:")
    answers1 = []
    for q, options in questions:
        answer1 = st.radio(q, options, key=f"q1_{q}")
        answers1.append(answer1)

    # Collect answers for "Her"
    st.subheader("Her Answers:")
    answers2 = []
    for q, options in questions:
        answer2 = st.radio(q, options, key=f"q2_{q}")
        answers2.append(answer2)

    if st.button("Calculate Personality Compatibility 💘", key="personality_btn"):
        # Calculate a compatibility score based on answers (simplified for demonstration)
        compatibility_score = sum([1 for ans1, ans2 in zip(answers1, answers2) if ans1 == ans2])
        st.success(f"Your personality compatibility score is: {compatibility_score * 20}%!")



# ---- TAB 3: AI Love Advice Chatbot ----
with tab3:
    st.header("💌 AI Love Advice")
    if st.button("Get Love Advice 💬", key="love_advice_btn"):
        advice = get_love_advice()
        st.info(advice)

# ---- TAB 4: Mini Games for Couples ----
with tab4:
    st.header("🎮 Love Game Time!")
    if st.button("Get a Fun Love Question 🎲", key="love_game_btn"):
        question = get_love_game()
        st.warning(question)

# ---- TAB 5: Love Story Compatibility ----
with tab5:
    st.header("💖 Love Story Compatibility")
    st.markdown(
        """
        Find out how compatible you are with your partner based on your love story.
        Answer the following questions and let's calculate your compatibility score!
        """
    )
    
    # Define love story questions
    story_questions = [
        ("Do you believe in love at first sight?", ["Yes", "No"]),
        ("How do you feel about long-distance relationships?", ["Works for me", "Not my thing"]),
        ("What’s more important in a relationship?", ["Trust", "Passion"]),
        ("How do you celebrate anniversaries?", ["Big celebrations", "Small, intimate moments"]),
        ("How do you handle challenges in your relationship?", ["Together, as a team", "It’s tough, but we try"]),
    ]
    
    answers1_story = []
    answers2_story = []
    
    # Collect answers for both partners
    st.subheader("Your Answers:")
    for q, options in story_questions:
        answer1 = st.radio(q, options, key=f"story_q1_{q}")
        answer2 = st.radio(q, options, key=f"story_q2_{q}")
        answers1_story.append(answer1)
        answers2_story.append(answer2)
    
    if st.button("Calculate Love Story Compatibility 💕", key="story_compat_btn"):
        # Calculate compatibility score based on answers (simplified for demonstration)
        story_compat_score = sum([1 for ans1, ans2 in zip(answers1_story, answers2_story) if ans1 == ans2])
        st.success(f"Your love story compatibility score is: {story_compat_score * 20}%!")


# ---- TAB 6: Love Story Generator ----
with tab6:
    st.header("📖 AI Love Story Generator")
    place = st.text_input("Where did you meet?", key="story_place")
    event = st.text_input("A special event in your relationship:", key="story_event")
    memory = st.text_input("A favorite shared memory:", key="story_memory")

    # Add image uploader
    uploaded_image = st.file_uploader("Upload Your Couple's Photo 📸", type=["jpg", "png", "jpeg"])

    if uploaded_image:
        st.image(uploaded_image, caption="Your Beautiful Moment ❤️", use_container_width=True)
        st.success("Such a cute photo! 💕")
        
    if st.button("Generate My Love Story ❤️", key="story_btn"):
        if name1 and name2 and place and event and memory:
            story = generate_ai_love_story(f"{name1} and {name2}", place, event, memory)
            st.success(story)
        else:
            st.warning("Please fill in all fields to generate your love story.")

# ---- TAB 7: Chat Sentiment Analysis ----
with tab7:
    st.header("💬 Chat Sentiment Check")
    chat_text = st.text_area("Paste your recent chat messages here:", key="chat_text")
    if st.button("Analyze Chat 💌", key="chat_btn"):
        sentiment_result = analyze_chat(chat_text)
        st.warning(sentiment_result)

# ---- TAB 8: Zodiac Compatibility ----
with tab8:
    st.header("✨ Zodiac Love Match")
    zodiac1 = st.selectbox("Select Your Zodiac Sign", ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"], key="zodiac1")
    zodiac2 = st.selectbox("Select Partner's Zodiac Sign", ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"], key="zodiac2")
    if st.button("Check Zodiac Compatibility 🌟", key="zodiac_btn"):
        st.success(zodiac_match(zodiac1, zodiac2))

# ---- TAB 9: Daily Love Challenge ----
with tab9:
    st.header("💖 Love Challenge of the Day")
    if st.button("Get Daily Love Challenge 🎯", key="love_challenge_btn"):
        challenge = daily_love_challenge()
        st.info(challenge)

st.markdown(
    """
    <style>
    /* Expander Header Styling */
    .streamlit-expanderHeader {
        font-size: 20px !important;
        font-weight: bold !important;
    }

    /* Tabs Styling */
    .tabs {
        display: flex;
        cursor: pointer;
        justify-content: space-around;
        font-size: 20px;
        font-weight: bold;
        padding: 10px;
        border-bottom: 2px solid #ccc;
    }

    .tabs div {
        padding: 10px;
    }

    .tabs div:hover {
        background-color: #f0f0f0;
    }

    .tabs div.active {
        border-bottom: 3px solid #00BFFF;
        color: #00BFFF;
    }

    /* Tab Button Styling */
    .css-1lcb2zz {
        font-size: 20px !important;
        font-weight: bold !important;
    }
    </style>
    """, unsafe_allow_html=True
)

