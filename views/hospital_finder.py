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
    st.markdown(
        """
        <style>
        .cognizant-banner {
            background: linear-gradient(90deg, #0050b3 60%, #1890ff 100%);
            color: #fff;
            padding: 2rem 1rem 1rem 1rem;
            border-radius: 18px;
            margin-bottom: 2rem;
            box-shadow: 0 4px 16px rgba(0,80,179,0.07);
        }
        .cognizant-card {
            background: #e6f7ff;
            border-radius: 14px;
            padding: 1.5rem 1.2rem;
            box-shadow: 0 2px 8px rgba(0,80,179,0.04);
            margin-bottom: 1.2rem;
        }
        .cognizant-metric {
            background: #f4faff;
            border-radius: 10px;
            padding: 0.7rem 1rem;
            font-size: 1.1rem;
            margin-bottom: 0.5rem;
            border-left: 5px solid #1890ff;
        }
        .cognizant-btn {
            background: linear-gradient(90deg, #0050b3 60%, #1890ff 100%);
            color: #fff !important;
            border: none;
            border-radius: 8px;
            padding: 0.7rem 1.2rem;
            font-weight: bold;
            font-size: 1.1rem;
            margin-top: 0.5rem;
        }
        </style>
        <div class='cognizant-banner'>
            <h1 style='margin-bottom:0.2em;'>🏥 Hospital Finder</h1>
            <span style='font-size:1.1em;'>Find the best care with Team Hyperscaler Solutions</span>
        </div>
        """,
        unsafe_allow_html=True
    )
    df = load_data()
    left_col, right_col = st.columns([3, 1])

    with left_col:
        st.markdown(
            """
            <div class='cognizant-card'>
            <h3 style='color:#0050b3;margin-bottom:0.7em;'>Search Hospitals</h3>
            """,
            unsafe_allow_html=True
        )
        postcode = st.text_input("Enter your postcode", placeholder="eg. SW1A 1AA")
        all_specialties = sorted({s.strip() for x in df['Specialties'].dropna() for s in x.split(",")})
        specialty = st.selectbox("Select a specialty", all_specialties)
        st.markdown("</div>", unsafe_allow_html=True)

        show_resource = False
        search_btn = st.button("🔍 Find Hospitals")
        if search_btn and postcode and specialty:
            coords = geocode_postcode(postcode)
            if coords:
                filtered = filter_by_specialty(df, specialty)
                results = add_distance(filtered, coords)
                st.markdown(
                    f"<div class='cognizant-card'><span style='color:#0050b3;font-weight:bold;'>Found {len(results)} hospitals offering {specialty}.</span></div>",
                    unsafe_allow_html=True
                )
                st.dataframe(results[['Hospital Name', 'Postcode', 'distance_km']])
                show_resource = True
            else:
                st.error("Failed to geocode postcode.")

    with right_col:
        if show_resource:
            st.markdown(
                """
                <div class='cognizant-card'>
                <h4 style='color:#0050b3;'>NHS Resources</h4>
                """,
                unsafe_allow_html=True
            )
            resource_url = NHS_RESOURCES.get(specialty)
            if specialty:
                resource_url = NHS_RESOURCES.get(specialty)
                if resource_url:
                    st.markdown(f"[Learn more about {specialty}]({resource_url})")
                else:
                    st.markdown(f"We are working on identifying resource for {specialty}.")
            st.markdown("</div>", unsafe_allow_html=True)