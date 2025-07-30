from geopy.distance import geodesic
import pandas as pd

def filter_by_specialty(df:pd.DataFrame,specialty:str)->pd.DataFrame:
    return df[df['Specialties'].str.contains(specialty, case=False, na=False)].copy()

def add_distance(df:pd.DataFrame,user_coords:tuple)->pd.DataFrame:
    df['distance_km'] = df.apply(lambda row: geodesic(user_coords, (row['lat'], row['lon'])).km, axis=1)
    return df.sort_values(by='distance_km').reset_index(drop=True)