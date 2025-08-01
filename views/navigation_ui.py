import streamlit as st

def inject_navigation_css():
    st.markdown("""
    <style>
    .nav-tile {
        background: #87ceeb;
        border-radius: 8px;
        padding: 1.1em 1.2em;
        margin-bottom: 0.6em;
        font-size: 1.13em;
        font-weight: 500;
        color: #22577a;
        border: none;
        box-shadow: none;
        display: block;
        text-align: center;
        text-decoration: none;
        width: 100%;
        height: 48px;
        line-height: 24px;
    }
    .sky-blue-tile {
        background: #87ceeb;
        color: #22577a;
    }
    
    .nav-tile:hover {
        background: #d7e8f7;
        color: #22577a;
    }
    .sidebar-nav-table {
        background: #eaf3fa;
        border: 1.5px solid #c2d3e8;
        border-radius: 8px;
        box-shadow: 0 1px 6px rgba(50, 90, 130, 0.04);
        padding: 0;
        margin: 0.6em 0 0.6em 0;
        display: flex;
        flex-direction: column;
        width: 100%;
    }
    .sidebar-nav-container {
        margin: 0;
        padding: 0;
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
