import streamlit as st

def inject_cognizant_css():
    st.markdown("""
        <style>
        div.stButton > button {
            background: linear-gradient(90deg, #0050b3 60%, #1890ff 100%);
            color: #fff !important;
            border: none;
            border-radius: 8px;
            padding: 0.9rem 1.5rem;
            font-weight: bold;
            font-size: 1.15rem;
            margin-top: 0.7rem;
            width: 100%;
            box-shadow: 0 2px 8px rgba(0,80,179,0.10);
            transition: background 0.2s;
        }
        div.stButton > button:hover {
            background: linear-gradient(90deg, #1890ff 60%, #0050b3 100%);
        }
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
            padding: 0.5rem 1.2rem;
            box-shadow: 0 2px 8px rgba(0,80,179,0.04);
            margin-bottom: 1.2rem;
        }
        </style>
    """, unsafe_allow_html=True)

def cognizant_banner(title, subtitle):
    st.markdown(f"""
        <div class='cognizant-banner'>
            <h1 style='margin-bottom:0.2em;'>{title}</h1>
            <span style='font-size:1.1em;'>{subtitle}</span>
        </div>
    """, unsafe_allow_html=True)

def search_hospitals_card():
    st.markdown("""
        <div class='cognizant-card'>
        <h3 style='color:#0050b3;margin-bottom:0.7em;'>Search Hospitals</h3>
    """, unsafe_allow_html=True)

def close_card():
    st.markdown("</div>", unsafe_allow_html=True)

def nhs_resources_card(resource_url, specialty):
    st.markdown("""
        <div class='cognizant-card' style='background:#f4faff; border:1.5px solid #0050b3;'>
            <h4 style='color:#0050b3;'>NHS Resources</h4>
    """, unsafe_allow_html=True)
    if resource_url:
        st.markdown(f"[Learn more about {specialty}]({resource_url})")
    else:
        st.markdown(f"We are working on identifying resource for {specialty}.")
    st.markdown("</div>", unsafe_allow_html=True)
