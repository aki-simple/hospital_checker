import streamlit as st
import pandas as pandas
import ssl
import certifi
ssl_context = ssl.create_default_context(cafile=certifi.where())

from geopy.geocoders import Nominatim
from geopy.adapters import AioHTTPAdapter
#from geopy.geocoders.options import default_ssl_context
from geopy.distance import geodesic

#default_ssl_context.check_hostname = False
##default_ssl_context.verify_mode = ssl.CERT_NONE

@st.cache_data
def load_hospitals():
    return pandas.read_csv("data/hospitals.csv")

@st.cache_data
def geocode_postcode(pc):
    geolocator = Nominatim(user_agent="hospital-finder")
    location = geolocator.geocode(pc)
    if location:
        return (location.latitude, location.longitude)
    else:
        return None
try:
    df= load_hospitals()
except Exception as e:
    st.error(f"Failed to load hospitals: {str(e)}")

st.set_page_config(page_title="Hospital Finder", page_icon=":hospital:")
st.title(":hospital: Hospital Finder")

postcode = st.text_input("Enter your postcode", placeholder="eg. SW1A 1AA")

specialties = sorted(df['specialty'].dropna().unique())
specialty = st.selectbox("Select a specialty", specialties)

if st.button("Find Hospitals"):
    if not postcode or not specialty:
        st.error("Please enter both postcode and specialty.")
    else:
        coords = geocode_postcode(postcode)

        if not coords:
            st.error("Failed to geocode postcode.")
        else:
            st.info(f"Your location: {coords}")

            filtered = df[df['specialty'] == specialty].copy()
            filtered['distance_km'] = filtered.apply(lambda row: geodesic(coords, (row['lat'], row['lon'])).km, axis=1)
            results = filtered.sort_values('distance_km').reset_index(drop=True)
            st.success(f"Found {len(results)} hospital(s) offering {specialty}.")
            st.dataframe(results[['name', 'postcode', 'distance_km']])
