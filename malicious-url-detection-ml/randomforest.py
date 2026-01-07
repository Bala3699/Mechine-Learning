import kagglehub
path = kagglehub.dataset_download("sid321axn/malicious-urls-dataset")
import os
import pandas as pd

# Download dataset
path = kagglehub.dataset_download("sid321axn/malicious-urls-dataset")

print("Dataset downloaded to:", path)
# TF-IDF Vectorization
vectorizer = TfidfVectorizer(max_features=5000)
X_vec = vectorizer.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X_vec, y, test_size=0.2, random_state=42
)

# Random Forest Model
rf_model = RandomForestClassifier(
    n_estimators=100,
    criterion="gini",
    random_state=42
)
rf_model.fit(X_train, y_train)

# Prediction
y_pred = rf_model.predict(X_test)

# Evaluation
print("Random Forest Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))
