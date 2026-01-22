# DDoS Detection using Machine Learning

## Overview
This project detects DDoS attacks using a Machine Learning approach.
A Linear Regression model is trained on real-time traffic data to
classify traffic as Normal or DDoS.

## Technologies Used
- Python
- Pandas
- Scikit-learn
- Matplotlib

## Project Structure
```
ddos-detection-ml/
│
├── data/
│   └── realtime_ddos_traffic_dataset.csv
│
├── src/
│   ├── ddos_detection.py
│   └── graph.py
│
├── requirements.txt
└── README.md
```  
## How to Run

### Step 1: Install Dependencies
```bash
pip install pandas scikit-learn matplotlib

python src/ddos_detection.py
```
## Output
-  Mean Squared Error (MSE)
-  Mean Absolute Error (MAE)
-  R² Score
-  Actual vs Predicted Traffic graph

## Label Encoding
-  Normal Traffic → 0
-  DDoS Traffic → 1

# Author

Balamurugan
B.Tech Computer Science & Engineering 
Cybersecurity / SOC Analyst Aspirant
