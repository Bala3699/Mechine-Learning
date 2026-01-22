# 🔐 Malicious URL Detection using Machine Learning

## 📌 Project Overview

This project focuses on detecting **malicious URLs** (Phishing, Malware, Defacement) using **Machine Learning (ML)** techniques. The system analyzes URL text patterns and classifies them as *benign* or *malicious* using supervised learning algorithms.

Two popular ML algorithms are implemented and evaluated:

* **Decision Tree Classifier**
* **Random Forest Classifier**

This project is suitable for **cybersecurity**, **ethical hacking**, and **ML-based intrusion detection** use cases.

---

## 🎯 Project Objectives

* To identify malicious URLs using machine learning
* To apply text vectorization (TF-IDF) on URLs
* To compare Decision Tree and Random Forest performance
* To build a beginner-friendly ML cybersecurity project

---

## 🧠 Machine Learning Algorithms Used

### 1️⃣ Decision Tree

* A tree-based supervised learning algorithm
* Uses Gini Index for splitting
* Fast and easy to interpret
* Can overfit on large datasets

### 2️⃣ Random Forest

* Ensemble learning method using multiple decision trees
* Reduces overfitting
* Higher accuracy and robustness
* Well-suited for cybersecurity datasets

---

## 📂 Dataset Information

* **Dataset Name:** Malicious URLs Dataset
* **Source:** Kaggle
* **File:** `malicious_phish.csv`
* **Features:**

  * `url` – URL string
  * `type` – benign / phishing / malware / defacement

The dataset contains a large number of real-world URLs used for training and testing ML models.

---

## ⚙️ Tools & Technologies

* Python 3.x
* KaggleHub
* Pandas
* NumPy
* Scikit-learn

---

## 🧪 Methodology

1. Download dataset using `kagglehub`
2. Load and explore the dataset
3. Convert URLs into numerical features using **TF-IDF Vectorizer**
4. Split data into training and testing sets
5. Train ML models (Decision Tree & Random Forest)
6. Evaluate models using accuracy and classification report

---

## 📊 Model Evaluation

* **Decision Tree:** Good accuracy, faster training
* **Random Forest:** Higher accuracy, better generalization

Random Forest performs better due to ensemble learning and reduced overfitting.

---

## ▶️ How to Run the Project

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 2: Run Decision Tree Program

```bash
python decision_tree.py
```

### Step 3: Run Random Forest Program

```bash
python random_forest.py
```

---

## 📦 requirements.txt

```text
kagglehub
pandas
numpy
scikit-learn
```

---

## 🔐 Cybersecurity Applications

* Phishing URL Detection
* Malware URL Classification
* Web Security Systems
* IDS / IPS systems
* Browser and Email Security Filters

---

## 🚀 Future Enhancements

* Feature engineering (URL length, digits, special characters)
* Confusion matrix visualization
* Model saving and deployment
* GUI integration
* Integration with CyberSentinel

---

## 👨‍💻 Author

**Balamurugan**
B.Tech CSE (Cybersecurity Enthusiast)

---

## ⚠️ Disclaimer

This project is created for **educational and research purposes only**. Do not use it for illegal activities.

---

⭐ If you find this project useful, please star the repository!
