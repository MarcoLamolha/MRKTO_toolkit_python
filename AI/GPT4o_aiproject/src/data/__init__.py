# File: /data-portfolio/data-portfolio/src/data/__init__.py

# This file contains functions for data loading and preprocessing.
# It utilizes Pandas for data manipulation and NumPy for numerical operations.

import pandas as pd
import numpy as np

def load_data(file_path):
    """Load data from a CSV file."""
    data = pd.read_csv(file_path)
    return data

def preprocess_data(data):
    """Preprocess the data by handling missing values and normalizing."""
    # Fill missing values with the mean of the column
    data.fillna(data.mean(), inplace=True)
    
    # Normalize numerical columns
    numerical_cols = data.select_dtypes(include=[np.number]).columns
    data[numerical_cols] = (data[numerical_cols] - data[numerical_cols].mean()) / data[numerical_cols].std()
    
    return data

def get_summary_statistics(data):
    """Return summary statistics of the dataset."""
    return data.describe()