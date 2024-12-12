import numpy as np
import os

def generate_synthetic_data(size=100, anomaly_fraction=0.1, save_path="../data/sensor_data.txt"):
    """
    Generate synthetic sensor data with a given fraction of anomalies.
    """
    np.random.seed(42)
    # Generate normal data
    normal_data = np.random.normal(0, 1, int(size * (1 - anomaly_fraction)))
    # Generate anomalies
    anomalies = np.random.uniform(-6, 6, int(size * anomaly_fraction))
    # Combine and shuffle
    data = np.concatenate([normal_data, anomalies])
    np.random.shuffle(data)
    
    # Save to file
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    np.savetxt(save_path, data, fmt="%.2f")
    print(f"Synthetic data saved to {save_path}")

if __name__ == "__main__":
    generate_synthetic_data()
