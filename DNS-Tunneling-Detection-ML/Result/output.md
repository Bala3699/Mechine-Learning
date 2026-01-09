## 📊 Results and Performance Evaluation

The machine learning models were evaluated using a train-test split of 80:20 on the CIC DNS traffic dataset containing over 1 million records.
---

### 🔹 Random Forest Classifier

* **Accuracy:** 99.99%
* Achieved very high precision and recall across all classes
* Effectively distinguished between benign and malicious DNS tunneling traffic
* Performed best due to its ability to handle high-dimensional network features
---

### 🔹 Support Vector Machine (SVM)

* **Accuracy:** 99.99%
* Successfully classified DNS tunneling patterns using a non-linear RBF kernel
* Slightly lower performance than Random Forest but still highly reliable
---

### 🔹 K-Means Clustering (Unsupervised)

* Used for anomaly detection without prior knowledge of labels
* Successfully grouped similar DNS traffic patterns
* Cluster labels did not directly map to attack labels, which is expected in unsupervised learning
---

### 📈 Model Comparison Summary
 
| Model         | Type         | Accuracy          |
| ------------- | ------------ | ----------------- |
| Random Forest | Supervised   | 99.99%            |
| SVM           | Supervised   | 99.99%            |
| K-Means       | Unsupervised | Anomaly Detection |
---
### ✅ Key Observation

Random Forest achieved the highest overall performance and is the most suitable model for DNS tunneling detection in this study.
