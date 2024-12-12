import os
import numpy as np
import joblib

# Get the root directory of the project
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_model(model_path="models/anomaly_model.pkl"):
    """
    Load the trained Isolation Forest model.
    """
    full_model_path = os.path.join(BASE_DIR, model_path)
    if not os.path.exists(full_model_path):
        raise FileNotFoundError(f"Model file not found at {full_model_path}")
    model = joblib.load(full_model_path)
    print(f"Model loaded from {full_model_path}")
    return model

def test_model(model, test_data):
    """
    Test the Isolation Forest model with new data.
    """
    predictions = model.predict(test_data.reshape(-1, 1))
    # Map predictions (-1 for anomaly, 1 for normal)
    result = ["Anomaly" if pred == -1 else "Normal" for pred in predictions]
    return result

def main():
    # Simulate new sensor data for testing
    test_data = np.array([48, 52, 75, 30, 55, 20, 65, 50])  # Example test data
    print(f"Testing data: {test_data}")

    try:
        # Load the trained model
        model = load_model()

        # Test the model
        results = test_model(model, test_data)

        # Display the results
        for value, status in zip(test_data, results):
            print(f"Value: {value:.2f}, Status: {status}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
