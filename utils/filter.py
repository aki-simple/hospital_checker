
import pandas as pd

def filter_by_specialty(df:pd.DataFrame,specialty:str)->pd.DataFrame:
    """
    Filters the DataFrame to include only rows where the 'Specialties' column contains the specified specialty.

    Parameters:
        df (pd.DataFrame): DataFrame containing hospital data with a 'Specialties' column.
        specialty (str): The specialty to filter by.

    Returns:
        pd.DataFrame: The filtered DataFrame containing only rows where the 'Specialties' column contains the specified specialty.
    """
    return df[df['Specialties'].str.contains(specialty, case=False, na=False)].copy()
