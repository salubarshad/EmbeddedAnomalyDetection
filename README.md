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
