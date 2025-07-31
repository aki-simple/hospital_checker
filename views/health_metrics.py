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
    Run the health metrics calculator app.
    """
    st.title("Health Metrics Calculator")

    left_col,right_col = st.columns([4,2])
    
    with left_col:
        with st.form("Health Form"):
            gender = st.selectbox("Gender", ["Select","Male", "Female"])
            age = st.number_input("Age (years)", min_value=0, max_value=120, value=0, step=1)
            height_cm = st.number_input("Height (cm)", min_value=0, max_value=250, value=0)
            weight_kg = st.number_input("Weight (kg)", min_value=0, max_value=200, value=0)
            activity_level = st.selectbox("Activity Level", ["Select","Sedentary", "Moderate", "Active"])
            submitted = st.form_submit_button("Calculate")

        if submitted:
            if gender == "Select" or activity_level == "Select" or age == 0 or height_cm == 0 or weight_kg == 0:
                st.error("Please fill all the fields.")
                return
            
            bmi,bmi_category = calculate_bmi(weight_kg,height_cm)
            rmr = calculate_rmr(gender,weight_kg,height_cm,age)
            
            multiplier = {
                "Sedentary": 1.1,
                "Moderate": 1.3,
                "Active": 1.5
            }[activity_level]

            adjusted_rmr = round(rmr * multiplier)
            
            reduction = adjusted_rmr - 350
            maintence = adjusted_rmr
            gain = adjusted_rmr + 350

            st.subheader("Results")
            st.metric("BMI", bmi, bmi_category)
            st.metric("Resting Metabolic RateMR", f"{rmr} kcal/day")
            st.metric("Adjusted for Activity Level", f"{adjusted_rmr} kcal/day")
            
            st.markdown("### 📊 Suggested Daily Calorie Intake")
            if bmi_category == "Sub Optimal":
                st.write(f" **Weight Gain**: **{gain} kcal/day** - approx. 3lbs/month")
            elif bmi_category == "Optimal":
                st.write(f" **Weight Loss**: **{reduction} kcal/day** - approx. 3lbs/month")
                st.write(f" **Maintenance**: **{maintence} kcal/day**")
                st.write(f" **Weight Gain**: **{gain} kcal/day** - approx. 3lbs/month")
            else:
                st.write(f" **Weight Loss**: **{reduction} kcal/day** - approx. 3lbs/month")
    
    with right_col:
        st.markdown("### NHS Resources")
        st.markdown("[🥚 Protein Intake](https://www.plymouthhospitals.nhs.uk/display-pil/pil-a-guide-to-increasing-your-protein-intake-8276/)")
        st.markdown("[🥗 5 a day](https://www.nhs.uk/live-well/eat-well/food-guidelines-and-food-labels/the-eatwell-guide/)")
        st.markdown("[🥬 Fibre Intake](https://www.nhs.uk/live-well/eat-well/how-to-get-more-fibre-into-your-diet/)")
        st.markdown("[🧴 Obesity treatment](https://www.nhs.uk/conditions/obesity/treatment/)")
        st.markdown("[💊 Weight management injections](https://www.england.nhs.uk/ourwork/prevention/obesity/medicines-for-obesity/weight-management-injections/)")