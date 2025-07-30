import pandas as pd
import time
from utils.geocode import geocode_postcode

def preprocess_hospital_data(raw_path,output_path, show_progress = False):
    df = pd.read_csv(raw_path)
    df["lat"],df["lon"] = None, None

    for idx, row in df.iterrows():
        lat, lon = geocode_postcode(row['Postcode'])
        df.at[idx, 'lat'] = lat
        df.at[idx, 'lon'] = lon
        time.sleep(0.5)
    df.to_csv(output_path, index=False)
    return df
