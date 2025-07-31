import streamlit as st

def calculate_bmi(weight_kg, height_cm):
    """
    Calculate the Body Mass Index (BMI) and its category based on weight and height.

    Args:
        weight_kg (float): Weight in kilograms.
        height_cm (float): Height in centimeters.

    Returns:
        tuple: A tuple containing the BMI value (rounded to 1 decimal place) and a string category.
            Categories:
                - "Sub Optimal" for BMI < 18.5
                - "Optimal" for 18.5 <= BMI < 25
                - "Above Optimal" for 25 <= BMI < 30
                - "Obesity" for BMI >= 30
    """
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    if bmi < 18.5:
        category = "Sub Optimal"
    elif bmi < 25:
        category = "Optimal"
    elif bmi < 30:
        category = "Above Optimal"
    else:
        category = "Obesity"
    return round(bmi,1), category

def calculate_rmr(gender,weight_kg,height_cm,age):
    """
    Calculate the Resting Metabolic Rate (RMR) based on gender, weight, height, and age.

    Args:
        gender (str): Gender ("Male" or "Female").
        weight_kg (float): Weight in kilograms.
        height_cm (float): Height in centimeters.
        age (int): Age in years.

    Returns:
        float: The calculated RMR value (rounded to 1 decimal place).
    """
    if gender == "Male":
        rmr = 10 * weight_kg + 6.25 * height_cm - 5 * age + 5
    else:
        rmr = 10 * weight_kg + 6.25 * height_cm - 5 * age - 161
    return round(rmr)

def run_health_metrics():
    """
    Run the health metrics calculator app with a modern layout.
    """
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
            <h1 style='margin-bottom:0.2em;'>🩺 Health Metrics Calculator</h1>
            <span style='font-size:1.1em;'>Empowering your health journey with Team Hyperscaler Solutions</span>
        </div>
        """,
        unsafe_allow_html=True
    )

    left_col, right_col = st.columns([4, 2])

    with left_col:
        with st.form("Health Form"):
            st.markdown(
                """
                <div class='cognizant-card'>
                <h3 style='color:#0050b3;margin-bottom:0.7em;'>Personal Details</h3>
                """,
                unsafe_allow_html=True
            )
            gender = st.selectbox("Gender", ["Select", "Male", "Female"])
            age = st.number_input("Age (years)", min_value=0, max_value=120, value=0, step=1)
            height_cm = st.number_input("Height (cm)", min_value=0, max_value=250, value=0)
            weight_kg = st.number_input("Weight (kg)", min_value=0, max_value=200, value=0)
            activity_level = st.selectbox("Activity Level", ["Select", "Sedentary", "Moderate", "Active"])
            st.markdown("</div>", unsafe_allow_html=True)
            # Custom styled Calculate button
            st.markdown("""
                <style>
                .cognizant-btn-custom {
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
                .cognizant-btn-custom:hover {
                    background: linear-gradient(90deg, #1890ff 60%, #0050b3 100%);
                }
                </style>
                <button class='cognizant-btn-custom' type='submit'>🚀 Calculate</button>
            """, unsafe_allow_html=True)
            submitted = False  # We'll use the form's submit event below

        # Streamlit form_submit_button must still be called for form logic
        submitted = st.form_submit_button(" ", help="Calculate your health metrics")

        if submitted:
            if gender == "Select" or activity_level == "Select" or age == 0 or height_cm == 0 or weight_kg == 0:
                st.error("Please fill all the fields.")
                return

            bmi, bmi_category = calculate_bmi(weight_kg, height_cm)
            rmr = calculate_rmr(gender, weight_kg, height_cm, age)

            multiplier = {
                "Sedentary": 1.2,
                "Moderate": 1.35,
                "Active": 1.5
            }[activity_level]

            adjusted_rmr = round(rmr * multiplier)
            maintence = adjusted_rmr
            reduction = adjusted_rmr - 350
            gain = adjusted_rmr + 350

            st.markdown("""
                <div class='cognizant-card' style='background:#fff; border:1.5px solid #1890ff; margin-top:1.5rem;'>
                    <h4 style='color:#0050b3;margin-bottom:0.8em;'>Results</h4>
            """, unsafe_allow_html=True)
            st.markdown(f"<div class='cognizant-metric'>BMI: <b>{bmi}</b> ({bmi_category})</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='cognizant-metric'>Resting Metabolic Rate (RMR): <b>{rmr} kcal/day</b></div>", unsafe_allow_html=True)
            st.markdown(f"<div class='cognizant-metric'>Adjusted for Activity Level: <b>{adjusted_rmr} kcal/day</b></div>", unsafe_allow_html=True)
            st.markdown("<hr style='margin:1em 0 0.7em 0;border-top:1.5px solid #e6f7ff;'>", unsafe_allow_html=True)
            st.markdown("<b>📊 Suggested Daily Calorie Intake</b>")
            if bmi_category == "Sub Optimal":
                st.success(f"Weight Gain: **{gain} kcal/day** - approx. 3lbs/month")
            elif bmi_category == "Optimal":
                st.info(f"Weight Loss: **{reduction} kcal/day** - approx. 3lbs/month")
                st.info(f"Maintenance: **{maintence} kcal/day**")
                st.success(f"Weight Gain: **{gain} kcal/day** - approx. 3lbs/month")
            else:
                st.warning(f"Weight Loss: **{reduction} kcal/day** - approx. 3lbs/month")
            st.markdown("</div>", unsafe_allow_html=True)
    
    with right_col:
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