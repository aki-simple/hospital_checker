import streamlit as st
from .health_metrics_ui import inject_cognizant_css, cognizant_banner, close_card, nhs_resources_card
import random
import pandas as pd
import plotly.express as px

from utils.constants import NHS_WELLBEING_RESOURCES, WELLBEING_TIPS, WELLBEING_IMAGES, WELLBEING_QUOTES, EMERGENCY_CONTACTS, SUPPORT_SUGGESTIONS

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
    cols = st.columns(len(NHS_WELLBEING_RESOURCES))
    for i, res in enumerate(NHS_WELLBEING_RESOURCES):
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
    # Image navigation with icon buttons 1,2,3...
    img_idx = 0
    cols = st.columns(len(WELLBEING_IMAGES))
    for i, col in enumerate(cols):
        if col.button(f"{i+1}", help=f"Show inspirational image {i+1}"):
            img_idx = i
    st.image(
        WELLBEING_IMAGES[img_idx], 
        use_container_width=True, 
        caption="Stay inspired!",
        output_format="auto"
    )  # Streamlit uses caption as alt text for accessibility
    st.markdown(f"<div style='font-style:italic;color:#0050b3;font-size:1.07em;'>{random.choice(WELLBEING_QUOTES)}</div>", unsafe_allow_html=True)
    close_card()

    # --- Rotating NHS-backed Tip ---
    st.markdown("<div class='cognizant-card'>", unsafe_allow_html=True)
    st.subheader("Tip of the Day")
    st.info(random.choice(WELLBEING_TIPS))
    close_card()

    # --- Emergency & Support Contacts ---
    st.markdown("<div class='cognizant-card'>", unsafe_allow_html=True)
    st.subheader("Emergency & Support Contacts")
    for contact in EMERGENCY_CONTACTS:
        st.markdown(f"<b>{contact['name']}</b>: <span style='color:#0050b3;font-weight:bold;'>{contact['contact']}</span> <span style='font-size:0.97em;'>({contact['desc']})</span>", unsafe_allow_html=True)
    close_card()

    # --- Community Poll / Event ---
    import pandas as pd
    import os
    POLL_FILE = os.path.join("data", "community_poll_votes.csv")
    poll_options = ["Exercise", "Talking to someone", "Healthy eating", "Sleep", "Nature", "Other"]

    st.markdown("<div class='cognizant-card'>", unsafe_allow_html=True)
    st.subheader("Community Poll")
    poll = st.radio("What helps your well-being most?", poll_options)
    vote_submitted = False

    if st.button("Submit Vote"):
        # Append vote to file
        try:
            if not os.path.exists(POLL_FILE):
                with open(POLL_FILE, "w") as f:
                    f.write("option\n")
            with open(POLL_FILE, "a") as f:
                f.write(f"{poll}\n")
            st.success("Thank you for sharing! Every voice matters.")
            vote_submitted = True
        except Exception as e:
            st.error(f"Error saving your vote: {e}")

    # Read and display poll results
    if os.path.exists(POLL_FILE):
        df_poll = pd.read_csv(POLL_FILE)
        results = df_poll['option'].value_counts().reindex(poll_options, fill_value=0)
        st.markdown("<hr style='margin:0.7em 0 0.7em 0;'>", unsafe_allow_html=True)
        st.markdown("**Community Poll Results:**")
        st.bar_chart(results)
    close_card()

    # --- NHS Resources Card (from health_metrics_ui for visual consistency) ---
    nhs_resources_card()

# To use this page, call run_wellbeing_page() from your Streamlit app.
