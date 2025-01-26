import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = "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"

# Function to generate travel itinerary
def generate_itinerary(user_inputs):
    try:
        messages = [
            {"role": "system", "content": "You are an AI travel assistant helping to create a personalized travel itinerary."},
            {"role": "user", "content": f"I want a travel itinerary with these details: {user_inputs}"}
        ]
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Or "gpt-3.5-turbo"
            messages=messages,
        )
        # Extract the assistant's message content
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Error generating itinerary: {e}"

# Streamlit UI
st.title("AI Travel Itinerary Planner")
st.markdown("### Create your personalized travel plan in just a few steps!")

# Input form with user details
with st.form("travel_form"):
    destination = st.text_input("Destination", "e.g., Paris")
    budget = st.text_input("Budget", "e.g., Moderate, Luxury, Budget")
    duration = st.number_input("Trip Duration (in days)", min_value=1, step=1)
    purpose = st.text_input("Purpose", "e.g., Leisure, Adventure, Relaxation")
    preferences = st.text_area("Preferences", "e.g., Historical sites, Beaches, Local food")
    dietary = st.text_input("Dietary Preferences", "e.g., Vegetarian, Vegan, Non-vegetarian")
    mobility = st.text_input("Mobility Concerns", "e.g., None, Low walking tolerance")
    submitted = st.form_submit_button("Generate Itinerary")

# Process user inputs and generate itinerary
if submitted:
    user_inputs = {
        "Destination": destination,
        "Budget": budget,
        "Duration": duration,
        "Purpose": purpose,
        "Preferences": preferences,
        "Dietary Preferences": dietary,
        "Mobility Concerns": mobility
    }
    st.write("### Generating your itinerary...")
    itinerary = generate_itinerary(user_inputs)
    st.markdown("### Your Travel Itinerary:")
    st.write(itinerary)

# Requirements.txt
txt = """
openai
streamlit
"""
with open("requirements.txt", "w") as file:
    file.write(txt)
