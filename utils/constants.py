import os

CLEAN_PATH = os.path.join("data", "hospitals_clean.csv")
RAW_PATH = os.path.join("data", "hospitals_london.csv")

POSTCODE_API = "https://api.postcodes.io/postcodes/{}"

GEOCODE_TIMEOUT = 5
DISTANCE_DECIMALS = 2

NHS_RESOURCES = {
    "Emergency care": ["https://www.nhs.uk/nhs-services/urgent-and-emergency-care-services/when-to-go-to-ae/"],
    "Hyperacute Stroke Unit": ["https://www.nhs.uk/conditions/stroke/"],
    "Heart Attack Centre": ["https://www.nhs.uk/conditions/heart-attack/"],
    "Neurology": ["https://www.nhs.uk/conditions/neurology/", "https://www.nhs.uk/conditions/"],
    "Neurosurgery": ["https://www.nhs.uk/conditions/neurosurgery/"],
    "Women’s Health": ["https://www.nhs.uk/conditions/pregnancy-and-baby/", "https://www.nhs.uk/conditions/gynaecological-cancer/"],
    "Urology": ["https://www.nhs.uk/conditions/urology/", "https://www.nhs.uk/conditions/prostate-cancer/"],
    "Dermatology": ["https://www.nhs.uk/conditions/skin-conditions/", "https://www.nhs.uk/conditions/eczema/"],
    "Respiratory Medicine": ["https://www.nhs.uk/conditions/respiratory-tract-infection/", "https://www.nhs.uk/conditions/asthma/"],
    "Rheumatology": ["https://www.nhs.uk/conditions/rheumatoid-arthritis/", "https://www.nhs.uk/conditions/lupus/"],
    "Endocrinology": ["https://www.nhs.uk/conditions/endocrine-glands/", "https://www.nhs.uk/conditions/thyroid-disease/"],
    "Diabetes": ["https://www.nhs.uk/conditions/diabetes/"],
    "Cardiology": ["https://www.nhs.uk/conditions/cardiovascular-disease/", "https://www.nhs.uk/conditions/heart-disease/"],
    "Tropical diseases": ["https://www.nhs.uk/conditions/tropical-diseases/", "https://www.nhs.uk/conditions/malaria/"],
    "Travel-related infections": ["https://www.nhs.uk/conditions/travel-vaccinations/", "https://www.nhs.uk/conditions/infectious-diseases/"],
    "Major Trauma": ["https://www.nhs.uk/conditions/trauma/"],
    "Emergency": ["https://www.nhs.uk/nhs-services/urgent-and-emergency-care-services/when-to-go-to-ae/"],
    "Stroke": ["https://www.nhs.uk/conditions/stroke/"],
    "Paediatrics": ["https://www.nhs.uk/conditions/baby/", "https://www.nhs.uk/conditions/childrens-health/"],
    "Haematology": ["https://www.nhs.uk/conditions/anaemia/", "https://www.nhs.uk/conditions/blood-cancer/"],
    "Plastics": ["https://www.nhs.uk/conditions/plastic-surgery/"],
    "Burns": ["https://www.nhs.uk/conditions/burns-and-scalds/"],
    "Dentistry": ["https://www.nhs.uk/nhs-services/dentists/"],
    "Oncology": ["https://www.nhs.uk/conditions/cancer/"],
    "Minor Injuries": ["https://www.nhs.uk/nhs-services/urgent-and-emergency-care-services/when-to-go-to-ae/"],
    "General Acute Services": ["https://www.nhs.uk/nhs-services/hospitals/"],
    "Maternity": ["https://www.nhs.uk/conditions/pregnancy-and-baby/"],
    "General Medicine": ["https://www.nhs.uk/conditions/"],
    "Surgery": ["https://www.nhs.uk/conditions/surgery/"],
    "General Services": ["https://www.nhs.uk/nhs-services/hospitals/"],
    "Orthopaedics": ["https://www.nhs.uk/conditions/orthopaedic-surgery/", "https://www.nhs.uk/conditions/arthritis/"],
    "Colorectal": ["https://www.nhs.uk/conditions/colorectal-cancer/", "https://www.nhs.uk/conditions/bowel-cancer/"],
    "Gastrointestinal": ["https://www.nhs.uk/conditions/gastroenteritis/", "https://www.nhs.uk/conditions/irritable-bowel-syndrome-ibs/"],
    "HIV": ["https://www.nhs.uk/conditions/hiv-and-aids/"],
    "Sexual Health": ["https://www.nhs.uk/live-well/sexual-health/"],
    "Hepatology": ["https://www.nhs.uk/conditions/liver-disease/"],
    "Fetal Medicine": ["https://www.nhs.uk/conditions/pregnancy-and-baby/antenatal-screening-tests/"],
    "Pancreatic Transplant": ["https://www.nhs.uk/conditions/pancreas-transplant/"],
    "Gene Therapy": ["https://www.nhs.uk/conditions/gene-therapy/"],
    "Rare Diseases": ["https://www.nhs.uk/conditions/rare-diseases/"],
    "Ophthalmology": ["https://www.nhs.uk/conditions/eye-surgery/", "https://www.nhs.uk/conditions/eye-problems/"],
    "Eye Surgery": ["https://www.nhs.uk/conditions/eye-surgery/"],
    "Rehabilitation": ["https://www.nhs.uk/conditions/rehabilitation/"],
    "Spinal Injury": ["https://www.nhs.uk/conditions/spinal-cord-injury/"],
    "Bone Tumours": ["https://www.nhs.uk/conditions/soft-tissue-sarcoma/", "https://www.nhs.uk/conditions/bone-cancer/"],
    "Cancer Research": ["https://www.nhs.uk/conditions/cancer/"],
}

# Well-being Page Constants
NHS_WELLBEING_RESOURCES = [
    {"title": "Every Mind Matters", "desc": "NHS mental health tips & self-assessment.", "url": "https://www.nhs.uk/every-mind-matters/", "icon": "🧠"},
    {"title": "Live Well", "desc": "NHS healthy living advice.", "url": "https://www.nhs.uk/live-well/", "icon": "💪"},
    {"title": "Mental Health", "desc": "NHS mental health support.", "url": "https://www.nhs.uk/mental-health/", "icon": "💬"},
    {"title": "ONS Well-being Data", "desc": "UK well-being statistics.", "url": "https://www.ons.gov.uk/peoplepopulationandcommunity/wellbeing", "icon": "📊"},
]

WELLBEING_TIPS = [
    "Drink enough water today! Hydration boosts mood and focus.",
    "Take a short walk – even 10 minutes helps your well-being.",
    "Try a 1-minute mindful breathing break.",
    "Connect with a friend or loved one today.",
    "Aim for 7-9 hours of sleep tonight.",
    "Eat a rainbow: add more colours to your plate.",
    "Limit screen time before bed for better sleep.",
    "Practice gratitude: write down one thing you're thankful for.",
]

WELLBEING_IMAGES = [
    "https://images.unsplash.com/photo-1506744038136-46273834b3fb",  # nature
    "https://images.unsplash.com/photo-1465101046530-73398c7f28ca",  # exercise
    "https://images.unsplash.com/photo-1517841905240-472988babdf9",  # community
    "https://images.unsplash.com/photo-1464983953574-0892a716854b",  # calm
]

WELLBEING_QUOTES = [
    "The greatest wealth is health. – Virgil",
    "Take care of your body. It's the only place you have to live. – Jim Rohn",
    "Self-care is not selfish. You cannot serve from an empty vessel.",
    "Well-being is not a destination, but a journey.",
]

EMERGENCY_CONTACTS = [
    {"name": "NHS 111 (Non-Emergency)", "contact": "111", "desc": "24/7 health advice."},
    {"name": "Samaritans", "contact": "116 123", "desc": "Mental health support, 24/7."},
    {"name": "Emergency Services", "contact": "999", "desc": "Medical, fire, police emergencies."},
]

SUPPORT_SUGGESTIONS = {
    "Stressed": "Consider reaching out to the NHS Every Mind Matters or Samaritans for support.",
    "Low": "Consider reaching out to the NHS Every Mind Matters or Samaritans for support.",
    "Meh": "Try a quick walk, a healthy snack, or connect with a friend!",
    "Great": "Keep up the positive energy! Maybe share your good mood with someone else.",
    "Okay": "Keep up the positive energy! Maybe share your good mood with someone else.",
}
