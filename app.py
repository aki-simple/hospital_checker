import streamlit as st
from views.hospital_finder import run_hospital_finder
from views.health_metrics import run_health_metrics
from views.wellbeing import run_wellbeing_page

st.set_page_config(page_title="Health Navigator", layout="centered")
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Choose page", [
    "Physical and Mental Wellbeing",
    "Hospital Finder",
    "Weight Management"
])

if selection == "Physical and Mental Wellbeing":
    run_wellbeing_page()
if selection == "Hospital Finder":
    run_hospital_finder()
if selection == "Weight Management":
    run_health_metrics()


