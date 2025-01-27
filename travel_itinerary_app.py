import streamlit as st
import openai
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
openai.api_key = os.getenv("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")

# Function to generate travel itinerary
def generate_itinerary(user_inputs):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Or "gpt-3.5-turbo"
            messages=[
                {"role": "system", "content": "You are an AI travel assistant helping to create a personalized travel itinerary."},
                {"role": "user", "content": f"Create a travel itinerary based on these details: {user_inputs}"}
            ],
        )
        return response.choices[0].message.content
    except Exception as e:
        st.error("Error generating itinerary. Please try again later.")
        return str(e)

# Streamlit UI setup
st.set_page_config(page_title="AI Travel Planner", page_icon="✈️", layout="wide")

# Add custom CSS for styling
st.markdown(
    """
    <style>
    body {
        background-color: #f5f7fa;
    }
    .main-title {
        font-family: 'Arial', sans-serif;
        color: #2c3e50;
        text-align: center;
        padding: 10px;
        background: linear-gradient(to right, #6dd5fa, #2980b9);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .description {
        font-size: 18px;
        text-align: center;
        color: #34495e;
        margin-bottom: 20px;
    }
    .stButton > button {
        background-color: #2980b9;
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 10px;
        font-size: 16px;
        cursor: pointer;
    }
    .stButton > button:hover {
        background-color: #3498db;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Banner image
st.image(
    "https://via.placeholder.com/1500x500.png?text=Plan+Your+Dream+Trip+Now",
    use_container_width=True,
)

# Main Title
st.markdown('<h1 class="main-title">AI Travel Itinerary Planner</h1>', unsafe_allow_html=True)

# Description
st.markdown(
    '<p class="description">Create your personalized travel plan effortlessly and make your journey unforgettable!</p>',
    unsafe_allow_html=True,
)

# Input form
with st.form("travel_form"):
    st.markdown("### 📝 Fill in Your Travel Details")
    col1, col2 = st.columns(2)

    with col1:
        destination = st.text_input("🌍 Destination", "e.g., Paris")
        budget = st.selectbox("💰 Budget", ["Moderate", "Luxury", "Budget"])
        duration = st.number_input("📅 Trip Duration (in days)", min_value=1, max_value=30, step=1)
        purpose = st.selectbox("🎯 Purpose", ["Leisure", "Adventure", "Relaxation"])

    with col2:
        preferences = st.text_area("🏖️ Preferences", "e.g., Historical sites, Beaches, Local food")
        dietary = st.selectbox("🥗 Dietary Preferences", ["Vegetarian", "Vegan", "Non-vegetarian"])
        mobility = st.text_input("♿ Mobility Concerns", "e.g., None, Low walking tolerance")

    submitted = st.form_submit_button("✨ Generate Itinerary")

# Displaying the generated itinerary
if submitted:
    user_inputs = {
        "Destination": destination,
        "Budget": budget,
        "Duration": duration,
        "Purpose": purpose,
        "Preferences": preferences,
        "Dietary Preferences": dietary,
        "Mobility Concerns": mobility,
    }
    with st.spinner("Generating your itinerary..."):
        itinerary = generate_itinerary(user_inputs)

    st.success("🎉 Your Travel Itinerary is Ready!")
    st.markdown("### 🌟 Your Travel Itinerary:")
    st.write(itinerary)

# requirements.txt content
txt = """
openai
streamlit
python-dotenv
"""
with open("requirements.txt", "w") as file:
    file.write(txt)
