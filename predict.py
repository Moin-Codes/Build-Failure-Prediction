import pandas as pd
import joblib

# Load trained model
model = joblib.load("models/build_failure_model.pkl")

print("===== BUILD FAILURE PREDICTION SYSTEM =====")

# Sample upcoming builds
builds = pd.DataFrame({
    "lines_changed": [50, 850],
    "files_changed": [3, 40],
    "previous_failures": [0, 8],
    "code_complexity": [10, 90],
    "test_failure_rate": [0.05, 0.85]
})

# Predict build status
predictions = model.predict(builds)
probabilities = model.predict_proba(builds)

for i in range(len(builds)):
    print(f"\nBuild {i + 1}")
    print("-------------------------")

    status = "FAIL" if predictions[i] == 1 else "PASS"

    print("Predicted Build Status:", status)
    print(f"Failure Probability: {probabilities[i][1] * 100:.2f}%")

    if predictions[i] == 1:
        print("Recommendation: Review code before building.")
    else:
        print("Recommendation: Proceed with normal build checks.")

print("\nPrediction completed successfully!")