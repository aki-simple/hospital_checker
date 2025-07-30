from geopy.distance import geodesic
import pandas as pd

def add_distance(df: pd.DataFrame, user_coords: tuple) -> pd.DataFrame:
    """
    Adds a 'distance_km' column to the DataFrame, representing the distance in kilometers from the user's coordinates to each hospital.

    Parameters:
        df (pd.DataFrame): DataFrame containing hospital data with 'lat' and 'lon' columns for latitude and longitude.
        user_coords (tuple): A tuple (latitude, longitude) representing the user's location.

    Returns:
        pd.DataFrame: The input DataFrame with an added 'distance_km' column, sorted by distance ascending and index reset.
    """
    
    df['distance_km'] = df.apply(lambda row: geodesic(user_coords, (row['lat'], row['lon'])).km, axis=1)
    return df.sort_values(by='distance_km').reset_index(drop=True)
