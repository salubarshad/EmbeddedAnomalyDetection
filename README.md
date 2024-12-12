# AI-based Anomaly Detection for Embedded Systems

This project implements an AI-based anomaly detection system, designed to be used with embedded systems like the **ESP32**. The system uses machine learning techniques to detect anomalies in sensor data, which could be useful in applications such as **IoT**, **predictive maintenance**, and **real-time monitoring**.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Technologies Used](#technologies-used)
3. [Data Generation](#data-generation)
4. [Model Training](#model-training)
5. [Model Testing](#model-testing)
6. [Usage](#usage)
7. [File Structure](#file-structure)
8. [License](#license)

## Project Overview

This project is designed to detect anomalies in sensor data using a machine learning model. The system follows a **three-step process**:

1. **Data Generation**: Synthetic sensor data is generated to simulate real-world sensor input.
2. **Model Training**: A machine learning model is trained using the generated data to detect anomalies.
3. **Model Testing**: The trained model is tested on a set of data to check its accuracy and predictions.

## Technologies Used

- **Python**: The primary programming language used to implement data generation, model training, and testing.
- **Scikit-learn**: A Python library used for training machine learning models like Random Forest.
- **Numpy**: Used for numerical operations, particularly for data manipulation and feature engineering.
- **Matplotlib**: Used for data visualization during exploratory data analysis and model evaluation.

## Data Generation

The first step of the project involves generating synthetic sensor data that mimics real-world sensor inputs. This data is created using random number generation and is saved to a file for further processing.

### Key Details:
- The data is generated as a text file (`sensor_data.txt`) with random values.
- Each entry in the data represents a sensor reading that could be used for anomaly detection in a system like IoT.
  
Run the `generate_data.py` script to generate the synthetic data:

```bash
python scripts/generate_data.py
```

## Model Training

Once the data is generated, the next step is to train a machine learning model on this data. In this case, we are using a Random Forest classifier, which is known for handling anomaly detection tasks well.

### Training Process:
- The data is loaded from the sensor_data.txt file.
- A Random Forest model is trained to predict anomalies in the sensor readings.
- The trained model is saved to a file (anomaly_model.pkl) for future use.

Run the train_model.py script to train the model:

```bash
python scripts/train_model.py
```

## Model Testing

After training the model, it's important to test its performance on unseen data. This is where the model’s accuracy and reliability are evaluated.

The testing script will load the trained model and apply it to a test dataset, providing predictions for each sensor reading.

### Testing Process:
- The trained model is loaded from the saved .pkl file.
- Test data is passed to the model, which returns predictions indicating whether each reading is an anomaly or normal.
- The results are printed to the console, displaying the sensor readings and their corresponding status.

Run the test_model.py script to test the model:

```bash
python scripts/test_model.py
```

## Usage

To use this project, follow the steps below:

1. Generate synthetic sensor data by running:
```bash
python scripts/generate_data.py
```
2. Train the anomaly detection model:
```bash
python scripts/train_model.py
```
3. Test the model's performance:
```bash
python scripts/test_model.py
```

Once these steps are completed, the model will be trained and tested, with results displayed on the console.

## File Structure

The project consists of the following files and folders:
```bash
/EmbeddedAnomalyDetection
    /data
        sensor_data.txt       # Generated sensor data
    /models
        anomaly_model.pkl     # Trained anomaly detection model
    /scripts
        generate_data.py      # Script for generating sensor data
        train_model.py        # Script for training the model
        test_model.py         # Script for testing the model
    README.md                 # Project documentation
```
