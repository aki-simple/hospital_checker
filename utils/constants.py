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

