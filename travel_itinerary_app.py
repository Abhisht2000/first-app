import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = "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"

# Function to generate travel itinerary
def generate_itinerary(user_inputs):
    try:
        # Corrected API call using `openai.ChatCompletion.create`
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Or "gpt-3.5-turbo"
            messages=[
                {"role": "system", "content": "You are an AI travel assistant helping to create a personalized travel itinerary."},
                {"role": "user", "content": f"Create a travel itinerary based on these details: {user_inputs}"}
            ],
        )
        return response.choices[0].message.content  # Correctly access the response content
    except Exception as e:
        return f"Error generating itinerary: {e}"


# Streamlit UI - Make it more visually appealing
st.set_page_config(page_title="AI Travel Planner", page_icon="✈️", layout="wide")

# Add a travel banner image
st.image("https://via.placeholder.com/1500x500.png?text=Your+Travel+Journey+Starts+Here", use_column_width=True)

# Title and description
st.markdown("""
    <h1 style="color: #2c3e50; text-align: center;">Welcome to AI Travel Itinerary Planner</h1>
    <p style="text-align: center; color: #34495e;">Create your personalized travel plan in just a few steps!</p>
""", unsafe_allow_html=True)

# Input form with user details - Layout improvement using columns
with st.form("travel_form"):
    col1, col2 = st.columns(2)

    with col1:
        destination = st.text_input("Destination", "e.g., Paris", help="Where would you like to travel?")
        budget = st.selectbox("Budget", ["Moderate", "Luxury", "Budget"], help="What is your budget?")
        duration = st.number_input("Trip Duration (in days)", min_value=1, step=1, help="How many days will your trip be?")
        purpose = st.selectbox("Purpose", ["Leisure", "Adventure", "Relaxation"], help="What is the purpose of your trip?")

    with col2:
        preferences = st.text_area("Preferences", "e.g., Historical sites, Beaches, Local food", help="Any specific places or activities?")
        dietary = st.selectbox("Dietary Preferences", ["Vegetarian", "Vegan", "Non-vegetarian"], help="Do you have dietary restrictions?")
        mobility = st.text_input("Mobility Concerns", "e.g., None, Low walking tolerance", help="Do you have any mobility concerns?")

    # Submit button inside the form
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
