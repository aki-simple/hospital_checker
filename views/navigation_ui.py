import streamlit as st

# NOTE: Do NOT inject global CSS or call st.set_page_config in any page-specific or UI helper file.
# Only inject CSS for the navigation pane here, and only call st.set_page_config in app.py.
def inject_navigation_css():
    st.markdown("""
    <style>
    /* Extra robust selector for sidebar navigation: targets both old and new Streamlit sidebar structures */
    aside[data-testid="stSidebar"] .nav-tile, section[data-testid="stSidebar"] .nav-tile, .stSidebar .nav-tile {
        background: #87ceeb !important;
        border-radius: 8px !important;
        padding: 1.1em 1.2em !important;
        margin-bottom: 0.6em !important;
        font-size: 1.13em !important;
        font-weight: 500 !important;
        color: #22577a !important;
        border: none !important;
        box-shadow: none !important;
        display: block !important;
        text-align: center !important;
        text-decoration: none !important;
        width: 100% !important;
        height: 48px !important;
        line-height: 24px !important;
    }
    aside[data-testid="stSidebar"] .sky-blue-tile, section[data-testid="stSidebar"] .sky-blue-tile, .stSidebar .sky-blue-tile {
        background: #87ceeb !important;
        color: #22577a !important;
    }
    aside[data-testid="stSidebar"] .nav-tile:hover, section[data-testid="stSidebar"] .nav-tile:hover, .stSidebar .nav-tile:hover {
        background: #d7e8f7 !important;
        color: #22577a !important;
    }
    </style>
    """, unsafe_allow_html=True)



def sidebar_nav(options, default=None):
    inject_navigation_css()
    if default is None:
        default = options[0]
    if 'nav_page' not in st.session_state:
        st.session_state['nav_page'] = default
    st.sidebar.markdown('<div style="font-weight:700;font-size:1.17em;color:#22577a;text-align:center;padding-top:0.7em;">Health Navigator</div>', unsafe_allow_html=True)
    st.sidebar.markdown('<hr style="margin:0.7em 0 1.1em 0; border:0; border-top:1.5px solid #c2d3e8;">', unsafe_allow_html=True)
    for option in options:
        if st.sidebar.button(option, key=f"nav-{option}"):
            st.session_state['nav_page'] = option
    return st.session_state['nav_page']
