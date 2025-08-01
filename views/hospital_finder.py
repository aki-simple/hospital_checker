import streamlit as st
from .hospital_finder_ui import inject_cognizant_css, cognizant_banner, search_hospitals_card, close_card, nhs_resources_card
import pandas as pandas
import os
from utils.geocode import geocode_postcode
from utils.filter import filter_by_specialty
from utils.distance import add_distance
from utils.constants import CLEAN_PATH, RAW_PATH, NHS_RESOURCES
from utils.preprocess import preprocess_hospital_data

@st.cache_data
def load_data():
    """
    Loads the hospital data from a CSV file, preprocessing it if necessary.

    Returns:
        pd.DataFrame: The preprocessed hospital data DataFrame.
    """
    if not os.path.exists(CLEAN_PATH):
        st.warning("Preprocessing data...")
        df = preprocess_hospital_data(RAW_PATH, CLEAN_PATH, show_progress=True)
        st.success("Data preprocessed.")
        return df
    return pandas.read_csv(CLEAN_PATH)

def run_hospital_finder():
    """
    Runs the hospital finder app with Cognizant branding and a modern layout.
    """
    st.set_page_config(page_title="Hospital Finder", page_icon=":hospital:")
    inject_cognizant_css()
    cognizant_banner("🏥 Hospital Finder", "Find the best care with Team Hyperscaler Solutions")
    df = load_data()
    left_col, right_col = st.columns([5, 2])

    with left_col:
        search_hospitals_card()
        postcode = st.text_input("Enter your postcode", placeholder="eg. SW1A 1AA")
        all_specialties = sorted({s.strip() for x in df['Specialties'].dropna() for s in x.split(",")})
        specialty = st.selectbox("Select a specialty", all_specialties)
        close_card()

        show_resource = False
        search_btn = st.button("🔍 Find Hospitals")
        if search_btn and postcode and specialty:
            coords = geocode_postcode(postcode)
            if coords:
                filtered = filter_by_specialty(df, specialty)
                results = add_distance(filtered, coords)
                # Filter for hospitals within 100 km
                within_100km = results[results['distance_km'] <= 100]
                if within_100km.empty:
                    st.warning("Unable to find any hospital in a 100 km radius.")
                else:
                    st.markdown(
                        f"<div class='cognizant-card'><span style='color:#0050b3;font-weight:bold;'>Found {len(results)} hospitals offering {specialty}.</span></div>",
                        unsafe_allow_html=True
                    )
                    st.dataframe(within_100km[['Hospital Name', 'Phone', 'Postcode', 'distance_km']], use_container_width=True, hide_index=True)
                show_resource = True
            else:
                st.error("Failed to geocode postcode.")

    with right_col:
        if show_resource:
            resource_url = NHS_RESOURCES.get(specialty)
            nhs_resources_card(resource_url, specialty)