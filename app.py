import streamlit as st
from views.hospital_finder import run_hospital_finder


st.set_page_config(page_title="Health Navigator", layout="centered")
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Choose page", [
    "Hospital Finder",
    "Physical and Mental Wellbeing",
    "Health Metrics"
])

if selection == "Hospital Finder":
    run_hospital_finder()
