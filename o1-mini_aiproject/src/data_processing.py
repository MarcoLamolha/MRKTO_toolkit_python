import pandas as pd
import numpy as np

def load_data(filepath):
    """Load data from a CSV file."""
    data = pd.read_csv(filepath)
    return data

def preprocess_data(data):
    """Preprocess the data."""
    # Handle missing values
    data.fillna(method='ffill', inplace=True)
    # Encode categorical variables
    data = pd.get_dummies(data)
    return data