import streamlit as st
from .health_metrics_ui import inject_cognizant_css, cognizant_banner, close_card, nhs_resources_card
import random
import pandas as pd
import plotly.express as px

# --- NHS and ONS Data Links ---
NHS_RESOURCES = [
    {"title": "Every Mind Matters", "desc": "NHS mental health tips & self-assessment.", "url": "https://www.nhs.uk/every-mind-matters/", "icon": "🧠"},
    {"title": "Live Well", "desc": "NHS healthy living advice.", "url": "https://www.nhs.uk/live-well/", "icon": "💪"},
    {"title": "Mental Health", "desc": "NHS mental health support.", "url": "https://www.nhs.uk/mental-health/", "icon": "💬"},
    {"title": "ONS Well-being Data", "desc": "UK well-being statistics.", "url": "https://www.ons.gov.uk/peoplepopulationandcommunity/wellbeing", "icon": "📊"},
]

TIPS = [
    "Drink enough water today! Hydration boosts mood and focus.",
    "Take a short walk – even 10 minutes helps your well-being.",
    "Try a 1-minute mindful breathing break.",
    "Connect with a friend or loved one today.",
    "Aim for 7-9 hours of sleep tonight.",
    "Eat a rainbow: add more colours to your plate.",
    "Limit screen time before bed for better sleep.",
    "Practice gratitude: write down one thing you're thankful for.",
]

IMAGES = [
    "https://images.unsplash.com/photo-1506744038136-46273834b3fb",  # nature
    "https://images.unsplash.com/photo-1465101046530-73398c7f28ca",  # exercise
    "https://images.unsplash.com/photo-1517841905240-472988babdf9",  # community
    "https://images.unsplash.com/photo-1464983953574-0892a716854b",  # calm
]

QUOTES = [
    "The greatest wealth is health. – Virgil",
    "Take care of your body. It's the only place you have to live. – Jim Rohn",
    "Self-care is not selfish. You cannot serve from an empty vessel.",
    "Well-being is not a destination, but a journey.",
]

EMERGENCY_CONTACTS = [
    {"name": "NHS 111 (Non-Emergency)", "contact": "111", "desc": "24/7 health advice."},
    {"name": "Samaritans", "contact": "116 123", "desc": "Mental health support, 24/7."},
    {"name": "Emergency Services", "contact": "999", "desc": "Medical, fire, police emergencies."},
]

# --- Example Data for Visualization ---
wellbeing_data = pd.DataFrame({
    "Year": [2021, 2022, 2023],
    "UK Life Satisfaction (1-10)": [7.1, 7.2, 7.0],
    "% Regular Exercise": [55, 57, 59],
    "% Good Sleep": [68, 70, 67],
})


def run_wellbeing_page():
    inject_cognizant_css()
    cognizant_banner("🌱 Well-being for Everyone", "Your guide to a healthier, happier you – powered by NHS and ONS data")
    
    st.markdown("<div class='cognizant-card'>", unsafe_allow_html=True)
    st.header("NHS & Trusted Resources")
    cols = st.columns(len(NHS_RESOURCES))
    for i, res in enumerate(NHS_RESOURCES):
        with cols[i]:
            st.markdown(f"<div style='padding:0.3em 0.7em;'><span style='font-size:2em;'>{res['icon']}</span> <b>{res['title']}</b><br><span style='font-size:0.98em;'>{res['desc']}</span><br><a href='{res['url']}' target='_blank' style='color:#0050b3;text-decoration:underline;'>Learn More</a></div>", unsafe_allow_html=True)
    close_card()
    
    # --- Interactive Mood Check ---
    st.markdown("<div class='cognizant-card'>", unsafe_allow_html=True)
    st.subheader("How are you feeling today?")
    mood = st.radio("Select your mood:", ["😊 Great", "🙂 Okay", "😐 Meh", "😟 Stressed", "😢 Low"], horizontal=True)
    if st.button("Get Support Suggestions"):
        if mood in ["😟 Stressed", "😢 Low"]:
            st.info("Consider reaching out to the NHS Every Mind Matters or Samaritans for support.")
        elif mood == "😐 Meh":
            st.info("Try a quick walk, a healthy snack, or connect with a friend!")
        else:
            st.success("Keep up the positive energy! Maybe share your good mood with someone else.")
    close_card()

    # --- Data-backed Visualizations ---
    st.markdown("<div class='cognizant-card'>", unsafe_allow_html=True)
    st.subheader("UK Well-being Trends (ONS Data)")
    fig = px.line(wellbeing_data, x="Year", y=["UK Life Satisfaction (1-10)", "% Regular Exercise", "% Good Sleep"],
                  markers=True, labels={"value":"Score / %", "variable":"Metric"})
    st.plotly_chart(fig, use_container_width=True)
    close_card()

    # --- Media Carousel (Image + Quote) ---
    st.markdown("<div class='cognizant-card'>", unsafe_allow_html=True)
    st.subheader("Inspiration & Positivity")
    img_idx = st.slider("Browse images:", 0, len(IMAGES)-1, 0)
    st.image(IMAGES[img_idx], use_column_width=True, caption="Stay inspired!")
    st.markdown(f"<div style='font-style:italic;color:#0050b3;font-size:1.07em;'>{random.choice(QUOTES)}</div>", unsafe_allow_html=True)
    close_card()

    # --- Rotating NHS-backed Tip ---
    st.markdown("<div class='cognizant-card'>", unsafe_allow_html=True)
    st.subheader("Tip of the Day")
    st.info(random.choice(TIPS))
    close_card()

    # --- Emergency & Support Contacts ---
    st.markdown("<div class='cognizant-card'>", unsafe_allow_html=True)
    st.subheader("Emergency & Support Contacts")
    for contact in EMERGENCY_CONTACTS:
        st.markdown(f"<b>{contact['name']}</b>: <span style='color:#0050b3;font-weight:bold;'>{contact['contact']}</span> <span style='font-size:0.97em;'>({contact['desc']})</span>", unsafe_allow_html=True)
    close_card()

    # --- Community Poll / Event ---
    st.markdown("<div class='cognizant-card'>", unsafe_allow_html=True)
    st.subheader("Community Poll")
    poll = st.radio("What helps your well-being most?", ["Exercise", "Talking to someone", "Healthy eating", "Sleep", "Nature", "Other"])
    if st.button("Submit Vote"):
        st.success("Thank you for sharing! Every voice matters.")
    close_card()

    # --- NHS Resources Card (from health_metrics_ui for visual consistency) ---
    nhs_resources_card()

# To use this page, call run_wellbeing_page() from your Streamlit app.
