# This file contains utility functions that assist with various tasks in the project.

def format_data(data):
    """Format the data for better readability."""
    return data.apply(lambda x: f"{x:.2f}" if isinstance(x, (int, float)) else x)

def log_message(message):
    """Log a message to the console."""
    print(f"[LOG] {message}")

def validate_data(data):
    """Validate the data for completeness and correctness."""
    if data.isnull().any().any():
        raise ValueError("Data contains null values.")
    return True