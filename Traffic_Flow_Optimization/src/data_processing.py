# src/data_processing.py

import pandas as pd
import yaml

# Load config file
with open('config/config.yaml', 'r') as file:
    config = yaml.safe_load(file)

def load_data():
    """Load raw traffic data."""
    raw_data_path = config['data']['raw_data_path']
    return pd.read_csv(raw_data_path)

def clean_data(df):
    """Clean and preprocess traffic data."""
    # Example cleaning steps
    df.dropna(inplace=True)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    return df

def preprocess_data(df):
    """Additional preprocessing, e.g., feature engineering."""
    df['hour'] = df['timestamp'].dt.hour
    df['day_of_week'] = df['timestamp'].dt.dayofweek
    return df

if __name__ == "__main__":
    data = load_data()
    data = clean_data(data)
    processed_data = preprocess_data(data)
    processed_data.to_csv(config['data']['processed_data_path'], index=False)
