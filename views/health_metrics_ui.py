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
            padding: 0.5rem 0.8rem 0.8rem 0.5rem;
            box-shadow: 0 2px 8px rgba(0,80,179,0.04);
            margin-bottom: 0.2rem;
        }
        .cognizant-metric {
            background: #f4faff;
            border-radius: 10px;
            padding: 0.7rem 1rem;
            font-size: 1.1rem;
            margin-bottom: 0.5rem;
            border-left: 5px solid #1890ff;
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

def personal_details_card():
    st.markdown("""
        <div class='cognizant-card'>
        <h3 style='color:#0050b3;margin-bottom:0.2em;'>Personal Details</h3>
    """, unsafe_allow_html=True)

def close_card():
    st.markdown("</div>", unsafe_allow_html=True)

def results_card(bmi, bmi_category, rmr, adjusted_rmr, gain, reduction, maintence):
    st.markdown("""
        <div class='cognizant-card' style='background:#fff; border:1.5px solid #1890ff;'>
            <h4 style='color:#0050b3;margin-bottom:0.5em;'>Results</h4>
    """, unsafe_allow_html=True)
    st.markdown(f"<div class='cognizant-metric'>BMI: <b>{bmi}</b> ({bmi_category})</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='cognizant-metric'>Resting Metabolic Rate (RMR): <b>{rmr} kcal/day</b></div>", unsafe_allow_html=True)
    st.markdown(f"<div class='cognizant-metric'>Adjusted for Activity Level: <b>{adjusted_rmr} kcal/day</b></div>", unsafe_allow_html=True)
    st.markdown("### 📊 Suggested Daily Calorie Intake")

def nhs_resources_card():
    st.markdown("""
        <div class='cognizant-card' style='background:#f4faff; border:1.5px solid #0050b3;'>
            <h4 style='color:#0050b3;'>NHS Resources</h4>
            <ul style='padding-left:1.1em;font-size:1.04em;'>
                <li>🥚 <a href='https://www.plymouthhospitals.nhs.uk/display-pil/pil-a-guide-to-increasing-your-protein-intake-8276/' target='_blank' style='color:#0050b3;text-decoration:underline;'>Protein Intake</a></li>
                <li>🥗 <a href='https://www.nhs.uk/live-well/eat-well/food-guidelines-and-food-labels/the-eatwell-guide/' target='_blank' style='color:#0050b3;text-decoration:underline;'>5 a day</a></li>
                <li>🥬 <a href='https://www.nhs.uk/live-well/eat-well/how-to-get-more-fibre-into-your-diet/' target='_blank' style='color:#0050b3;text-decoration:underline;'>Fibre Intake</a></li>
                <li>🧴 <a href='https://www.nhs.uk/conditions/obesity/treatment/' target='_blank' style='color:#0050b3;text-decoration:underline;'>Obesity treatment</a></li>
                <li>💊 <a href='https://www.england.nhs.uk/ourwork/prevention/obesity/medicines-for-obesity/weight-management-injections/' target='_blank' style='color:#0050b3;text-decoration:underline;'>Weight management injections</a></li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
