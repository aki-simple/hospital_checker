import streamlit as st
import pandas as pandas
import os
from utils.geocode import geocode_postcode
from utils.filter import filter_by_specialty, add_distance
from utils.preprocess import preprocess_hospital_data

CLEAN_PATH = "data/hospitals_clean.csv"
RAW_PATH = "data/hospitals_london.csv"

@st.cache_data
def load_data():
    if not os.path.exists(CLEAN_PATH):
        st.warning("Preprocessing data...")
        df = preprocess_hospital_data(RAW_PATH, CLEAN_PATH, show_progress=True)
        st.success("Data preprocessed.")
        return df
    return pandas.read_csv(CLEAN_PATH)

df = load_data()

st.set_page_config(page_title="Hospital Finder", page_icon=":hospital:")
st.title(":hospital: Hospital Finder")

postcode = st.text_input("Enter your postcode", placeholder="eg. SW1A 1AA")

all_specialties = sorted({s.strip() for x in df['Specialties'].dropna() for s in x.split(",")})
specialty = st.selectbox("Select a specialty", all_specialties)

if st.button("Find Hospitals") and postcode and specialty:
    coords = geocode_postcode(postcode)
    if coords:
        filtered = filter_by_specialty(df, specialty)
        results = add_distance(filtered, coords)
        st.success(f"Found {len(results)} hospitals offering {specialty}.")
        st.dataframe(results[['Hospital Name', 'Postcode', 'distance_km']])
    else:
        st.error("Failed to geocode postcode.")
    