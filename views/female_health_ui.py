import streamlit as st

def female_health_underrep_card():
    st.markdown("""
        <div style='background:#f5f2ff; border-left:6px solid #7c3aed; border-radius:10px; padding:1.2em 1em 1em 1.3em; margin-bottom:1.5em; box-shadow:0 2px 8px rgba(124,58,237,0.08);'>
            <span style='font-size:1.15em; font-weight:700; color:#7c3aed;'>Did you know?</span><br>
            <span style='font-size:1.05em; color:#333;'>
                <b>Only 2% of global health research funding</b> is dedicated to reproductive health (BMJ, 2020), and women are <b>underrepresented in 80% of clinical trials</b> for conditions that affect both sexes (FDA, 2022).<br><br>
                <i>This underrepresentation leads to delayed diagnoses, less effective treatments, and gaps in care for millions of women worldwide.</i>
            </span>
        </div>
    """, unsafe_allow_html=True)

import datetime

def cycle_phase_info(last_period, cycle_length):
    today = datetime.date.today()
    days_since_last = (today - last_period).days
    if days_since_last < 0:
        return None, None, None, None  # Invalid future date
    # Standard phase lengths (can be refined)
    period_len = 5
    follicular_len = 9  # (day 6-14)
    ovulation_len = 1   # (day 15)
    luteal_len = cycle_length - (period_len + follicular_len + ovulation_len)
    if days_since_last < period_len:
        phase = "Menstrual"
        one_liner = "You are in your Menstrual phase."
        mental = "You may feel more introspective or low energy; it's normal to want rest."
        physical = "Physical energy is often lowest; cramps or fatigue are common. Prioritize gentle self-care."
    elif days_since_last < period_len + follicular_len:
        phase = "Follicular"
        one_liner = "You are in your Follicular phase."
        mental = "Cognitive sharpness and creativity are rising; it's a great time for planning and new tasks."
        physical = "Physical energy is increasing; you may feel lighter and more motivated for activity."
    elif days_since_last < period_len + follicular_len + ovulation_len:
        phase = "Ovulation"
        one_liner = "You are in your Ovulation phase."
        mental = "Confidence and sociability are at their peak; communication comes easily."
        physical = "You may feel your strongest and most energetic; ideal for challenging workouts."
    elif days_since_last < cycle_length:
        phase = "Luteal"
        one_liner = "You are in your Luteal phase."
        mental = "Mood may fluctuate; it's normal to feel more sensitive or need downtime."
        physical = "Bloating or breast tenderness can occur; moderate exercise and healthy snacks help."
    else:
        phase = "Cycle Restart"
        one_liner = "Your cycle may have restarted; please check your dates."
        mental = "Cycle data may be off; review your last period date."
        physical = "Cycle data may be off; review your last period date."
    return phase, one_liner, mental, physical

def cycle_tracking_form():
    st.markdown("""
        <div style='background:#e6f7ff; border-radius:14px; box-shadow:0 2px 8px rgba(0,80,179,0.04); padding:0.9em 1.3em 0.7em 1.3em; margin-bottom:1.2em; width:100%;'>
            <span style='font-size:1.16em; font-weight:700; color:#0050b3;'>Cycle Tracking</span>
        </div>
    """, unsafe_allow_html=True)
    with st.form(key="cycle_form"):
        col1, col2 = st.columns([1,1])
        with col1:
            last_period = st.date_input("Date of Last Period", key="last_period")
        with col2:
            avg_cycle_length = st.number_input("Avg. Cycle Length", min_value=15, max_value=45, value=28, step=1, key="avg_cycle_length")
        submitted = st.form_submit_button("Submit")
        if submitted:
            phase, one_liner, mental, physical = cycle_phase_info(last_period, avg_cycle_length)
            if phase:
                st.markdown(f"<div style='margin-top:0.7em; margin-bottom:0.1em; font-size:1.08em; color:#22577a; font-weight:600;'>{one_liner}</div>", unsafe_allow_html=True)
                st.markdown(f"""
                    <div style='background:#eaf3fa; border-radius:8px; border:1px solid #c2d3e8; padding:0.7em 1.3em 0.7em 1.3em; margin-bottom:0.5em; width:100%;'>
                        <span style='font-size:1.01em; font-weight:600; color:#22577a;'>Your day today</span><br>
                        <ul style='margin:0.3em 0 0 1.1em; padding:0; color:#22577a; font-size:0.99em;'>
                            <li>{mental}</li>
                            <li>{physical}</li>
                        </ul>
                    </div>
                """, unsafe_allow_html=True)

                # --- PHASE-BASED EXERCISE & FOOD RECOMMENDATIONS ---
                # All suggestions below are based on scientific literature and clinical recommendations:
                # Menstrual: [ACOG, 2021; J Womens Health (Larchmt). 2019]
                # Follicular/Ovulation/Luteal: [ACOG, 2021; J Strength Cond Res. 2016; Nutrients. 2020]
                phase_exercises = {
                    "Menstrual": [
                        "Gentle yoga or stretching (ACOG, 2021)",
                        "Short walks or low-intensity movement (J Womens Health, 2019)"
                    ],
                    "Follicular": [
                        "Aerobic/cardio exercise (running, cycling) (J Strength Cond Res, 2016)",
                        "Strength/resistance training (Nutrients, 2020)"
                    ],
                    "Ovulation": [
                        "High-intensity interval training (HIIT) (J Strength Cond Res, 2016)",
                        "Group sports or dance (peak coordination) (Nutrients, 2020)"
                    ],
                    "Luteal": [
                        "Moderate-intensity exercise (pilates, swimming) (ACOG, 2021)",
                        "Gentle yoga or walking (ACOG, 2021)"
                    ],
                    "Cycle Restart": [
                        "Gentle movement (ACOG, 2021)",
                        "Rest and self-care (J Womens Health, 2019)"
                    ]
                }
                phase_foods = {
                    "Menstrual": [
                        "Iron-rich foods (spinach, lentils) (ACOG, 2021)",
                        "Hydrating foods & fluids (watermelon, cucumber) (ACOG, 2021)"
                    ],
                    "Follicular": [
                        "Lean protein (chicken, tofu) (Nutrients, 2020)",
                        "Complex carbs (quinoa, oats) (Nutrients, 2020)"
                    ],
                    "Ovulation": [
                        "Zinc-rich foods (pumpkin seeds, chickpeas) (Nutrients, 2020)",
                        "Antioxidant-rich berries (Nutrients, 2020)"
                    ],
                    "Luteal": [
                        "Magnesium-rich foods (dark chocolate, nuts) (J Womens Health, 2019)",
                        "Complex carbs (sweet potatoes, oats) (Nutrients, 2020)"
                    ],
                    "Cycle Restart": [
                        "Balanced, gentle foods (ACOG, 2021)",
                        "Plenty of water (ACOG, 2021)"
                    ]
                }
                exercises = phase_exercises.get(phase, phase_exercises["Cycle Restart"])
                foods = phase_foods.get(phase, phase_foods["Cycle Restart"])
                col_ex, col_food = st.columns(2)
                with col_ex:
                    st.markdown("<div style='font-size:1.06em; font-weight:600; color:#22577a; margin-bottom:0.3em;'>Exercises you can try</div>", unsafe_allow_html=True)
                    st.markdown("<ul style='margin:0 0 0 1.1em; padding:0; color:#22577a; font-size:0.99em;'>" + ''.join([f"<li>{ex}</li>" for ex in exercises]) + "</ul>", unsafe_allow_html=True)
                with col_food:
                    st.markdown("<div style='font-size:1.06em; font-weight:600; color:#22577a; margin-bottom:0.3em;'>Foods that help</div>", unsafe_allow_html=True)
                    st.markdown("<ul style='margin:0 0 0 1.1em; padding:0; color:#22577a; font-size:0.99em;'>" + ''.join([f"<li>{fd}</li>" for fd in foods]) + "</ul>", unsafe_allow_html=True)

                # NHS resources card will be rendered after this function, outside the container.
            else:
                st.error("Invalid last period date. Please check your input.")

# NHS resources card for Female Health, matching Wellbeing style

def female_health_nhs_resources_card():
    st.markdown("""
        <div style='background:#fff; border:2.5px solid #005eb8; border-radius:16px; margin:0.7em 0 1.2em 0; box-shadow:0 2px 12px rgba(0,94,184,0.08); padding:0.5em 0.5em 0.2em 0.5em;'>
            <h3 style='color:#005eb8; font-family:sans-serif; font-weight:800; margin:0 0 0.2em 0;'>NHS Resources</h3>
            <ul style='padding-left:2.5em; padding-bottom:1em; font-size:1em; font-family:sans-serif; color:#222;'>
                <li style='margin-bottom:0.3em;'><a href='https://www.nhs.uk/conditions/periods/' target='_blank' style='color:#005eb8;font-weight:bold;text-decoration:underline;'>Menstrual Cycle: NHS Guide</a></li>
                <li style='margin-bottom:0.3em;'><a href='https://www.nhs.uk/live-well/exercise/' target='_blank' style='color:#005eb8;font-weight:bold;text-decoration:underline;'>Exercise for Health</a></li>
                <li style='margin-bottom:0.3em;'><a href='https://www.nhs.uk/live-well/eat-well/' target='_blank' style='color:#005eb8;font-weight:bold;text-decoration:underline;'>Healthy Eating</a></li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    
