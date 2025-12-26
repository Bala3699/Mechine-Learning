# 🌐 Real-Time DDoS Detection Using Machine Learning

## 📌 Overview

This project implements a **machine learning–based DDoS detection system** using real-time network traffic data. The objective is to identify and distinguish **Normal traffic** from **DDoS attack traffic** by analyzing traffic behavior such as packet flow and byte rates. The project serves as a **baseline cybersecurity + ML implementation** suitable for SOC and security analyst roles.

---

## 🎯 Objectives

* Detect DDoS attacks using machine learning techniques
* Preprocess network traffic data for ML models
* Apply stratified sampling to preserve class balance
* Evaluate model performance using standard metrics
* Visualize prediction results

---

## 📊 Dataset Description

The dataset contains network traffic statistics collected under normal conditions and simulated DDoS attack scenarios.

**Key Features:**

* `packet_count`
* `packet_count_per_second`
* `byte_count`
* `byte_count_per_second`

**Label:**

* `traffic_type`

  * `0` → Normal Traffic
  * `1` → DDoS Traffic

---

## ⚙️ Methodology

* Label encoding of categorical traffic labels
* Feature–label separation
* Stratified train-test split (80% training, 20% testing)
* Linear Regression used as a **baseline model**
* Model evaluation using regression metrics
* Visualization of actual vs predicted values

---

## 📈 Evaluation Metrics

The model is evaluated using:

* **Mean Squared Error (MSE)**
* **Mean Absolute Error (MAE)**
* **R² Score (Coefficient of Determination)**

These metrics help measure prediction accuracy and model fit.

---

## 📉 Visualization

An **Actual vs Predicted** scatter plot is used to visualize how closely the model predictions align with the true traffic labels.

---

## 🧪 Results Summary

* Low error values indicate strong separation between normal and DDoS traffic
* Demonstrates effectiveness of traffic-based features
* Serves as a baseline for more advanced classification models

---

## 🛠️ Technologies Used

* **Python**
* **Pandas**
* **Scikit-learn**
* **Matplotlib**
* **Machine Learning**
* **Cybersecurity / Network Traffic Analysis**

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
python ddos_detection.py
python graph.py
```

---

## ⚠️ Limitations

* Linear Regression is not a classification algorithm
* Dataset may contain simulated attack patterns
* Not suitable for direct real-world deployment without further validation

---

## 🚀 Future Enhancements

* Implement Logistic Regression, Random Forest, or SVM
* Add confusion matrix, ROC curve, and F1-score
* Integrate real-time traffic capture (PCAP/Wireshark)
* Deploy as a real-time intrusion detection module

---

## 📌 Conclusion

This project demonstrates how machine learning can be applied to detect DDoS attacks using network traffic features. It provides a solid foundation for further research and development in intrusion detection systems and cybersecurity analytics.
