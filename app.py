import streamlit as st
from views.hospital_finder import run_hospital_finder
from views.health_metrics import run_health_metrics

st.set_page_config(page_title="Health Navigator", layout="centered")
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Choose page", [
    "Hospital Finder",
    "Physical and Mental Wellbeing",
    "Weight Management"
])

if selection == "Hospital Finder":
    run_hospital_finder()
if selection == "Weight Management":
    run_health_metrics()
