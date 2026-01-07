import kagglehub
path = kagglehub.dataset_download("sid321axn/malicious-urls-dataset")
import os
import pandas as pd

# Download dataset
path = kagglehub.dataset_download("sid321axn/malicious-urls-dataset")

print("Dataset downloaded to:", path)
import pandas as pd
import os

dataset_path = os.path.join(path, 'malicious_phish.csv') # Assuming the CSV file is named malicious_phish.csv inside the downloaded directory
df = pd.read_csv(dataset_path)
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report


print(df.head())

X = df["url"]
y = df["type"]

# TF-IDF Vectorization
vectorizer = TfidfVectorizer(max_features=5000)
X_vec = vectorizer.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X_vec, y, test_size=0.2, random_state=42
)

# Decision Tree Model
dt_model = DecisionTreeClassifier(criterion="gini", random_state=42)
dt_model.fit(X_train, y_train)

# Prediction
y_pred = dt_model.predict(X_test)

# Evaluation
print("Decision Tree Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))
