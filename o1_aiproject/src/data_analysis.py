import pandas as pd

def analyze_data(df: pd.DataFrame):
    print("Data shape:", df.shape)
    print("Data description:", df.describe())