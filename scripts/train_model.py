import numpy as np
from sklearn.ensemble import IsolationForest
import joblib
import os

def load_data(file_path="../data/sensor_data.txt"):
    """
    Load sensor data from a file.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Data file not found at {file_path}")
    data = np.loadtxt(file_path)
    print(f"Loaded data from {file_path}. Number of samples: {len(data)}")
    return data

def train_and_save_model(data, save_path="../models/anomaly_model.pkl"):
    """
    Train an Isolation Forest model and save it to a file.
    """
    model = IsolationForest(n_estimators=100, contamination=0.1, random_state=42)
    model.fit(data.reshape(-1, 1))
    
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    joblib.dump(model, save_path)
    print(f"Model trained and saved to {save_path}")

if __name__ == "__main__":
    try:
        # Load data
        data = load_data()
        
        # Train model
        train_and_save_model(data)
    except Exception as e:
        print(f"Error: {e}")
