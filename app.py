import streamlit as st
from views.hospital_finder import run_hospital_finder
from views.health_metrics import run_health_metrics
from views.wellbeing import run_wellbeing_page
from views.female_health import run_female_health_page

st.set_page_config(page_title="Health Navigator", layout="centered")
from views.navigation_ui import sidebar_nav

options = [
    "Wellbeing",
    "Female Health",
    "Hospital Finder",
    "Weight Management"
]
page = sidebar_nav(options, "Wellbeing")

if page == "Wellbeing":
    run_wellbeing_page()
elif page == "Female Health":
    run_female_health_page()
elif page == "Hospital Finder":
    run_hospital_finder()
elif page == "Weight Management":
    run_health_metrics()


