# src/evaluation.py

import numpy as np
from sklearn.metrics import accuracy_score

def evaluate_congestion_reduction(traffic_data, optimized_schedule):
    """Calculate congestion reduction after optimization."""
    baseline_congestion = np.mean(traffic_data)
    optimized_congestion = np.mean(traffic_data * optimized_schedule)
    return baseline_congestion - optimized_congestion

def evaluate_route_model(model, X_test, y_test):
    """Evaluate route optimization model accuracy."""
    y_pred = model.predict(X_test)
    return accuracy_score(y_test, y_pred)
