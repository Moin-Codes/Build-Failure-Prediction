import pandas as pd
import numpy as np

np.random.seed(42)

n = 1000

data = pd.DataFrame({
    "lines_changed": np.random.randint(10, 1000, n),
    "files_changed": np.random.randint(1, 50, n),
    "previous_failures": np.random.randint(0, 10, n),
    "code_complexity": np.random.randint(1, 100, n),
    "test_failure_rate": np.random.uniform(0, 1, n).round(2)
})

# Calculate build failure risk
risk = (
    data["lines_changed"] / 1000 * 0.20
    + data["files_changed"] / 50 * 0.15
    + data["previous_failures"] / 10 * 0.25
    + data["code_complexity"] / 100 * 0.15
    + data["test_failure_rate"] * 0.25
)

# Assign build status with simulated randomness
noise = np.random.normal(0, 0.08, n)
data["build_failed"] = ((risk + noise) > 0.5).astype(int)

data.to_csv("data/build_history.csv", index=False)

print("Dataset generated successfully!")
print("Total build records:", len(data))

print("\nSample Dataset:")
print(data.head())

print("\nBuild Status Distribution:")
print(data["build_failed"].value_counts())