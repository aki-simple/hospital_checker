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

def nhs_resources_card(resource_urls, specialty):
    st.markdown("""
        <div style='background:#fff; border:2.5px solid #005eb8; border-radius:16px; margin:0.7em 0 1.2em 0; box-shadow:0 2px 12px rgba(0,94,184,0.08); padding:0.5em 0.5em 0.2em 0.5em;'>
        <h3 style='color:#005eb8; font-family:sans-serif; font-weight:800; margin:0 0 0.2em 0;'>NHS Resources</h3>
    """, unsafe_allow_html=True)
    if resource_urls and isinstance(resource_urls, list) and len(resource_urls) > 0:
        st.markdown("<ul style='padding-left:1.3em;'>", unsafe_allow_html=True)
        for url in resource_urls:
            # Use the last part of the URL path as the link text
            label = url.rstrip('/').split('/')[-1].replace('-', ' ').capitalize()
            st.markdown(f"<li><a href='{url}' target='_blank' style='color:#005eb8;font-weight:bold;text-decoration:underline;font-size:1.07em;'>{label}</a></li>", unsafe_allow_html=True)
        st.markdown("</ul>", unsafe_allow_html=True)
    elif resource_urls and isinstance(resource_urls, str):
        st.markdown(f"<a href='{resource_urls}' target='_blank' style='color:#005eb8;font-weight:bold;text-decoration:underline;font-size:1.07em;'>Learn more about {specialty}</a>", unsafe_allow_html=True)
    else:
        st.markdown(f"<span style='font-size:1.07em;'>We are working on identifying resource for <b>{specialty}</b>.</span>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
