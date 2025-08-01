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

def health_metrics_results_card(bmi, bmi_category, rmr, adjusted_rmr):
    """
    Modern results card: BMI, RMR, Adjusted RMR in three columns.
    """
    st.markdown("<div class='cognizant-card' style='background:#fff; border:1.5px solid #1890ff;'>", unsafe_allow_html=True)
    st.markdown("<h4 style='color:#0050b3;margin-bottom:0.5em;'>Your Health Metrics</h4>", unsafe_allow_html=True)
    results_cols = st.columns(3)
    with results_cols[0]:
        st.markdown(f"""
        <div style='background:#e6f7ff; border-radius:10px; padding:0.7em 0.5em; border-left:5px solid #1890ff; text-align:center;'>
            <span style='font-size:1.07em; color:#0050b3; font-weight:bold;'>BMI</span><br>
            <span style='font-size:1.3em; color:#222; font-weight:bold;'>{bmi}</span><br>
            <span style='font-size:0.97em; color:#888;'>{bmi_category}</span>
        </div>
        """, unsafe_allow_html=True)
    with results_cols[1]:
        st.markdown(f"""
        <div style='background:#e6f7ff; border-radius:10px; padding:0.7em 0.5em; border-left:5px solid #1890ff; text-align:center;'>
            <span style='font-size:1.07em; color:#0050b3; font-weight:bold;'>RMR</span><br>
            <span style='font-size:1.3em; color:#222; font-weight:bold;'>{rmr} kcal/day</span><br>
            <span style='font-size:0.97em; color:#888;'>Resting Metabolic Rate</span>
        </div>
        """, unsafe_allow_html=True)
    with results_cols[2]:
        st.markdown(f"""
        <div style='background:#e6f7ff; border-radius:10px; padding:0.7em 0.5em; border-left:5px solid #1890ff; text-align:center;'>
            <span style='font-size:1.07em; color:#0050b3; font-weight:bold;'>Adj. RMR</span><br>
            <span style='font-size:1.3em; color:#222; font-weight:bold;'>{adjusted_rmr} kcal/day</span><br>
            <span style='font-size:0.97em; color:#888;'>For Activity Level</span>
        </div>
        """, unsafe_allow_html=True)
    close_card()

def suggested_calorie_intake_card(bmi_category, gain, maintence, reduction):
    """
    Dynamic suggested daily calorie intake card (shows only relevant cards based on BMI category).
    """
    st.markdown("<div class='cognizant-card' style='background:#fff; border:1.5px solid #1890ff; margin-top:1em;'>", unsafe_allow_html=True)
    st.markdown("<h4 style='color:#0050b3;margin-bottom:0.5em;'>Suggested Daily Calorie Intake</h4>", unsafe_allow_html=True)
    if bmi_category == "Sub Optimal":
        intake_cols = st.columns(2)
        # Weight Gain
        with intake_cols[0]:
            st.markdown(f"""
            <div style='background:#e6f7ff; border-radius:10px; padding:0.7em 0.5em; border-left:5px solid #52c41a; text-align:center; box-shadow:0 0 0 3px #52c41a55;'>
                <span style='font-size:1.07em; color:#52c41a; font-weight:bold;'>Weight Gain</span><br>
                <span style='font-size:1.3em; color:#222; font-weight:bold;'>{gain} kcal/day</span><br>
                <span style='font-size:0.97em; color:#888;'>(~3lbs/month)</span>
            </div>
            """, unsafe_allow_html=True)
        # Maintenance
        with intake_cols[1]:
            st.markdown(f"""
            <div style='background:#e6f7ff; border-radius:10px; padding:0.7em 0.5em; border-left:5px solid #0050b3; text-align:center;'>
                <span style='font-size:1.07em; color:#0050b3; font-weight:bold;'>Maintenance</span><br>
                <span style='font-size:1.3em; color:#222; font-weight:bold;'>{maintence} kcal/day</span>
            </div>
            """, unsafe_allow_html=True)
    elif bmi_category == "Optimal":
        intake_cols = st.columns(3)
        # Weight Gain
        with intake_cols[0]:
            st.markdown(f"""
            <div style='background:#e6f7ff; border-radius:10px; padding:0.7em 0.5em; border-left:5px solid #52c41a; text-align:center;'>
                <span style='font-size:1.07em; color:#52c41a; font-weight:bold;'>Weight Gain</span><br>
                <span style='font-size:1.3em; color:#222; font-weight:bold;'>{gain} kcal/day</span><br>
                <span style='font-size:0.97em; color:#888;'>(~3lbs/month)</span>
            </div>
            """, unsafe_allow_html=True)
        # Maintenance
        with intake_cols[1]:
            st.markdown(f"""
            <div style='background:#e6f7ff; border-radius:10px; padding:0.7em 0.5em; border-left:5px solid #0050b3; text-align:center;'>
                <span style='font-size:1.07em; color:#0050b3; font-weight:bold;'>Maintenance</span><br>
                <span style='font-size:1.3em; color:#222; font-weight:bold;'>{maintence} kcal/day</span>
            </div>
            """, unsafe_allow_html=True)
        # Weight Loss
        with intake_cols[2]:
            st.markdown(f"""
            <div style='background:#e6f7ff; border-radius:10px; padding:0.7em 0.5em; border-left:5px solid #fa541c; text-align:center;'>
                <span style='font-size:1.07em; color:#fa541c; font-weight:bold;'>Weight Loss</span><br>
                <span style='font-size:1.3em; color:#222; font-weight:bold;'>{reduction} kcal/day</span><br>
                <span style='font-size:0.97em; color:#888;'>(~3lbs/month)</span>
            </div>
            """, unsafe_allow_html=True)
    else:  # Above Optimal or Obesity
        intake_cols = st.columns(1)
        with intake_cols[0]:
            st.markdown(f"""
            <div style='background:#e6f7ff; border-radius:10px; padding:0.7em 0.5em; border-left:5px solid #fa541c; text-align:center; box-shadow:0 0 0 3px #fa541c55;'>
                <span style='font-size:1.07em; color:#fa541c; font-weight:bold;'>Weight Loss</span><br>
                <span style='font-size:1.3em; color:#222; font-weight:bold;'>{reduction} kcal/day</span><br>
                <span style='font-size:0.97em; color:#888;'>(~3lbs/month)</span>
            </div>
            """, unsafe_allow_html=True)
    close_card()

def nhs_resources_card():
    with st.container():
        st.markdown("""
            <div style='background:#fff; border:2.5px solid #005eb8; border-radius:16px; margin:0.7em 0 1.2em 0; box-shadow:0 2px 12px rgba(0,94,184,0.08); padding:0.5em 0.5em 0.2em 0.5em;'>
            """, unsafe_allow_html=True)
        st.markdown("<h3 style='color:#005eb8; font-family:sans-serif; font-weight:800; margin:0 0 0.2em 0;'>NHS Resources</h3>", unsafe_allow_html=True)
        st.markdown("""
            <ul style='padding-left:2.5em; padding-bottom:1em; font-size:1em; font-family:sans-serif; color:#222;'>
                <li style='margin-bottom:0.3em;'>🍽️ <a href='https://www.nhs.uk/live-well/eat-well/food-guidelines-and-food-labels/the-eatwell-guide/' target='_blank' style='color:#005eb8;font-weight:bold;text-decoration:underline;'>The Eatwell Guide</a></li>
                <li style='margin-bottom:0.3em;'>🥦 <a href='https://www.nhs.uk/live-well/eat-well/8-tips-for-healthy-eating/' target='_blank' style='color:#005eb8;font-weight:bold;text-decoration:underline;'>8 Tips for Healthy Eating</a></li>
                <li style='margin-bottom:0.3em;'>🍏 <a href='https://www.nhs.uk/live-well/eat-well/5-a-day/' target='_blank' style='color:#005eb8;font-weight:bold;text-decoration:underline;'>5 A Day</a></li>
                <li style='margin-bottom:0.3em;'>🌾 <a href='https://www.nhs.uk/live-well/eat-well/how-to-get-more-fibre-into-your-diet/' target='_blank' style='color:#005eb8;font-weight:bold;text-decoration:underline;'>How to Get More Fibre</a></li>
                <li style='margin-bottom:0.3em;'>🥗 <a href='https://www.nhs.uk/live-well/eat-well/' target='_blank' style='color:#005eb8;font-weight:bold;text-decoration:underline;'>Food and Diet</a></li>
                <li style='margin-bottom:0.3em;'>🔥 <a href='https://www.nhs.uk/live-well/eat-well/understanding-calories/' target='_blank' style='color:#005eb8;font-weight:bold;text-decoration:underline;'>Understanding Calories</a></li>
                <li style='margin-bottom:0.3em;'>🍽️ <a href='https://www.nhs.uk/live-well/eat-well/portion-size-guide/' target='_blank' style='color:#005eb8;font-weight:bold;text-decoration:underline;'>Portion Sizes</a></li>
                <li style='margin-bottom:0.3em;'>🍲 <a href='https://www.nhs.uk/healthier-families/recipes/' target='_blank' style='color:#005eb8;font-weight:bold;text-decoration:underline;'>Healthy Recipes</a></li>
                <li style='margin-bottom:0.3em;'>🏷️ <a href='https://www.nhs.uk/live-well/eat-well/food-labels/' target='_blank' style='color:#005eb8;font-weight:bold;text-decoration:underline;'>Food Labels</a></li>
                <li style='margin-bottom:0.3em;'>🥕 <a href='https://www.nhs.uk/live-well/eat-well/vegetarian-and-vegan-diets/' target='_blank' style='color:#005eb8;font-weight:bold;text-decoration:underline;'>Vegetarian and Vegan Diets</a></li>
                <li style='margin-bottom:0.3em;'>🥚 <a href='https://www.plymouthhospitals.nhs.uk/display-pil/pil-a-guide-to-increasing-your-protein-intake-8276/' target='_blank' style='color:#005eb8;font-weight:bold;text-decoration:underline;'>Protein Intake</a></li>
                <li style='margin-bottom:0.3em;'>🧴 <a href='https://www.nhs.uk/conditions/obesity/treatment/' target='_blank' style='color:#005eb8;font-weight:bold;text-decoration:underline;'>Obesity Treatment</a></li>
                <li style='margin-bottom:0.3em;'>💊 <a href='https://www.england.nhs.uk/ourwork/prevention/obesity/medicines-for-obesity/weight-management-injections/' target='_blank' style='color:#005eb8;font-weight:bold;text-decoration:underline;'>Weight Management Injections</a></li>
            </ul>
            </div>
        """, unsafe_allow_html=True)
