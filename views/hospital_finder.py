import streamlit as st
import pandas as pandas
import os
from utils.geocode import geocode_postcode
from utils.filter import filter_by_specialty
from utils.distance import add_distance
from utils.constants import CLEAN_PATH, RAW_PATH, NHS_RESOURCES
from utils.preprocess import preprocess_hospital_data

@st.cache_data
def load_data():
    if not os.path.exists(CLEAN_PATH):
        st.warning("Preprocessing data...")
        df = preprocess_hospital_data(RAW_PATH, CLEAN_PATH, show_progress=True)
        st.success("Data preprocessed.")
        return df
    return pandas.read_csv(CLEAN_PATH)

def run_hospital_finder():
    st.set_page_config(page_title="Hospital Finder", page_icon=":hospital:")

    df = load_data()
    left_col,right_col = st.columns([3,1])

    with left_col:
        st.title(":hospital: Hospital Finder")

        postcode = st.text_input("Enter your postcode", placeholder="eg. SW1A 1AA")

        all_specialties = sorted({s.strip() for x in df['Specialties'].dropna() for s in x.split(",")})
        specialty = st.selectbox("Select a specialty", all_specialties)

        show_resource = False

        if st.button("Find Hospitals") and postcode and specialty:
            coords = geocode_postcode(postcode)
            if coords:
                filtered = filter_by_specialty(df, specialty)
                results = add_distance(filtered, coords)
                st.success(f"Found {len(results)} hospitals offering {specialty}.")
                st.dataframe(results[['Hospital Name', 'Postcode', 'distance_km']])
                show_resource = True
            else:
                st.error("Failed to geocode postcode.")
    
    with right_col:
        if show_resource:
            st.markdown(f"## NHS Resources")
            resource_url = NHS_RESOURCES.get(specialty)
            if specialty:
               resource_url = NHS_RESOURCES.get(specialty)
               if resource_url:
                   st.markdown(f"[Learn more about {specialty}]({resource_url})")
               else:
                   st.markdown(f"We are working on identifying resource for {specialty}.")
        