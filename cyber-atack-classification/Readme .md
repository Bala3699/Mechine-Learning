# Cybersecurity Attack Detection using Logistic Regression

## Overview
This project focuses on detecting cybersecurity attacks using a machine learning approach.  
A **Logistic Regression** model is used to perform **binary classification**, identifying whether a given network traffic record represents an **attack (1)** or **normal traffic (0)**.

The dataset used is a **synthetic cybersecurity attacks dataset** provided by **Incribo**, designed to closely simulate real-world cyber traffic and attack patterns.

---

## Dataset Description
- **Name:** Cybersecurity Attacks Dataset
- **Source:** Incribo
- **License:** Apache 2.0
- **Records:** ~40,000
- **Features:** 25
- **Type:** Tabular (CSV)
- **Update Frequency:** Monthly

### Sample Features
- Timestamp  
- Source IP Address  
- Destination IP Address  
- Source Port  
- Destination Port  
- Protocol  
- Packet Length  
- Traffic Type  
- Anomaly Scores  
- Attack Type  
- Severity Level  

---

## Problem Statement
Linear regression models are not suitable for classification tasks because they attempt to fit a straight line and may produce values outside the range of 0 and 1.  
To overcome this limitation, **Logistic Regression** is used, which applies a **Sigmoid activation function** to produce outputs between 0 and 1, making it suitable for binary classification.

---

## Machine Learning Approach

### Model
- Logistic Regression

### Activation Function
The sigmoid function is used to map values between 0 and 1:

σ(z) = 1 / (1 + e⁻ᶻ)

### Classification Logic
- Output ≥ 0.5 → Attack (1)
- Output < 0.5 → Normal (0)

This makes the model a **binary classifier**.

---

## Project Structure

```
cyber_attack_classification/
│
├── data/
│ └── cybersecurity_attacks.csv
│
├── src/
│ └── logistic_model.py
│
├── requirements.txt
└── README.md

```

---

## Installation
Clone the repository and install the required dependencies.

git clone https://github.com/Bala3699/cyber-attack-classification.git

cd cyber-attack-classification
pip install -r requirements.tx


---

## Usage
Run the model using the following command:



---

## Model Workflow
1. Load the dataset
2. Clean and preprocess data
3. Encode categorical features
4. Scale numerical features
5. Split data into training and testing sets
6. Train logistic regression model
7. Generate predictions using sigmoid output
8. Apply threshold-based classification
9. Evaluate performance

---

## Evaluation Metrics
- Accuracy
- Confusion Matrix
- Precision
- Recall
- F1-Score

A heatmap visualization is used to analyze model performance.

---

## Applications
- Cyber attack detection
- SOC Level-1 alert analysis
- Network anomaly detection
- Machine learning–based IDS support

---

## Limitations
- Dataset is synthetic
- Only binary classification is implemented
- No real-time packet capture

---

## Future Improvements
- Multi-class attack classification
- Advanced ML/DL models
- Real-time network traffic analysis
- Feature importance and optimization

---

## License
This project uses a dataset licensed under the **Apache 2.0 License**.  
Refer to the original dataset source for detailed license information.

---

## Author
Balamurugan  
B.Tech – Computer Science and Engineering  
Cybersecurity & SOC Analyst Aspirant

