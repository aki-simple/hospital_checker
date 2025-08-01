import streamlit as st
import random
from .health_metrics_ui import inject_cognizant_css, cognizant_banner, personal_details_card, close_card, nhs_resources_card

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
    Run the health metrics calculator app with a modern layout and enhanced UX.
    """
    inject_cognizant_css()
    cognizant_banner("🩺 Health Metrics Calculator", "Empowering your health journey with Team Hyperscaler Solutions")
    form_col, nhs_col = st.columns([5, 3])
    with form_col:
        with st.form("Health Form"):
            personal_details_card()
            st.markdown("<span style='font-size:0.97em;color:#666;'>Please enter your details below. All fields are required.</span>", unsafe_allow_html=True)
            gender = st.selectbox("Gender", ["Select", "Male", "Female"], help="Select your gender")
            age = st.number_input("Age", min_value=0, max_value=120, value=0, step=1, help="Enter your age in years")
            height_cm = st.number_input("Height", min_value=0, max_value=250, value=0, help="Enter your height in centimeters (cm)")
            weight_kg = st.number_input("Weight", min_value=0, max_value=200, value=0, help="Enter your weight in kilograms (kg)")
            activity_level = st.selectbox("Activity Level", ["Select", "Sedentary", "Moderate", "Active"], help="Choose your typical activity level")
            st.caption("👤 Gender | 🎂 Age (years) | 📏 Height (cm) | ⚖️ Weight (kg) | 🚶 Activity Level")
            close_card()
            submitted = st.form_submit_button("🚀 Calculate", help="Calculate your health metrics")

    with nhs_col:
        nhs_resources_card()

    if submitted:
        errors = []
        if gender == "Select":
            errors.append("Please select your gender.")
        if activity_level == "Select":
            errors.append("Please select your activity level.")
        if age <= 0:
            errors.append("Please enter a valid age.")
        if height_cm <= 0:
            errors.append("Please enter a valid height (cm).")
        if weight_kg <= 0:
            errors.append("Please enter a valid weight (kg).")
        if errors:
            for err in errors:
                st.error(err)
            return

        bmi, bmi_category = calculate_bmi(weight_kg, height_cm)
        rmr = calculate_rmr(gender, weight_kg, height_cm, age)
        multiplier = {"Sedentary": 1.2, "Moderate": 1.35, "Active": 1.5}[activity_level]
        adjusted_rmr = round(rmr * multiplier)
        maintence = adjusted_rmr
        reduction = adjusted_rmr - 350
        gain = adjusted_rmr + 350

        from .health_metrics_ui import health_metrics_results_card, suggested_calorie_intake_card
        health_metrics_results_card(bmi, bmi_category, rmr, adjusted_rmr)
        suggested_calorie_intake_card(bmi_category, gain, maintence, reduction)