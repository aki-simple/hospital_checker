
import pandas as pd

def filter_by_specialty(df:pd.DataFrame,specialty:str)->pd.DataFrame:
    return df[df['Specialties'].str.contains(specialty, case=False, na=False)].copy()
