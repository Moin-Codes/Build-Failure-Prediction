import pandas as pd
import matplotlib.pyplot as plt
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    ConfusionMatrixDisplay
)

# Load dataset
data = pd.read_csv("data/build_history.csv")

# Separate features and target
X = data.drop("build_failed", axis=1)
y = data["build_failed"]

# Split dataset into 80% training and 20% testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42,
    stratify=y
)

# Train Random Forest model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate model
accuracy = accuracy_score(y_test, y_pred)

print("===== BUILD FAILURE PREDICTION =====")
print("Training records:", len(X_train))
print("Testing records:", len(X_test))
print(f"Model Accuracy: {accuracy * 100:.2f}%")

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Save confusion matrix
ConfusionMatrixDisplay.from_predictions(
    y_test, y_pred,
    display_labels=["PASS", "FAIL"],
    cmap="Blues"
)

plt.title("Build Failure Prediction - Confusion Matrix")
plt.tight_layout()
plt.savefig("results/confusion_matrix.png")
plt.close()

# Save trained model
joblib.dump(model, "models/build_failure_model.pkl")

print("\nModel saved successfully!")
print("Confusion matrix saved successfully!")