import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

# Example data (replace with real y_test and y_pred)
y_test = [0, 1, 0, 1, 1, 0]
y_pred = [0.1, 0.9, 0.2, 1.0, 0.8, 0.05]

plt.scatter(y_test, y_pred)
plt.xlabel("Actual Traffic Type (0 = Normal, 1 = DDoS)")
plt.ylabel("Predicted Value")
plt.title("Actual vs Predicted DDoS Traffic")

plt.show()
