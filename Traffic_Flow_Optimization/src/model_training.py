# src/model_training.py

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pandas as pd
import yaml

with open('config/config.yaml', 'r') as file:
    config = yaml.safe_load(file)

def train_route_model():
    """Train a model to suggest optimal routes based on traffic data."""
    data = pd.read_csv(config['data']['processed_data_path'])
    X = data[['hour', 'day_of_week', 'traffic_density', 'accidents']]
    y = data['route_choice']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy: {accuracy}")
    return model

