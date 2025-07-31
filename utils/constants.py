import os

CLEAN_PATH = os.path.join("data", "hospitals_clean.csv")
RAW_PATH = os.path.join("data", "hospitals_london.csv")

POSTCODE_API = "https://api.postcodes.io/postcodes/{}"

GEOCODE_TIMEOUT = 5
DISTANCE_DECIMALS = 2

NHS_RESOURCES ={
    "Cardiology": "https://www.nhs.uk/conditions/cardiovascular-disease/"
}
