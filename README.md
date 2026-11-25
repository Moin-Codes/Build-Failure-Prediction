# Build-Failure Prediction

## Project Overview
Build-Failure Prediction is a machine learning system that predicts whether a software build will pass or fail based on historical build-related metrics.

## Objectives
- Predict potential software build failures.
- Identify high-risk code changes.
- Improve CI/CD reliability.
- Support proactive failure prevention.

## Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Joblib
- Git and GitHub

## Machine Learning Algorithm
Random Forest Classifier.

## Dataset Features
- Lines changed
- Files changed
- Previous build failures
- Code complexity
- Historical test failure rate

## Model Performance

| Metric | Result |
|---|---:|
| Total records | 1000 |
| Training records | 800 |
| Testing records | 200 |
| Model accuracy | 82% |
| Weighted precision | 82% |
| Weighted recall | 82% |
| Weighted F1-score | 82% |

## Execution Steps
1. Install dependencies: `pip install -r requirements.txt`
2. Generate dataset: `python generate_dataset.py`
3. Train model: `python train_model.py`
4. Predict build status: `python predict.py`

## Limitations
The model is trained on synthetic build-history data. Real-world CI/CD data is required to validate production performance.

## Conclusion
The project demonstrates how machine learning can identify potential software build failures and support proactive decision-making in DevOps environments.

## Student Details
- Name: Mohammed Moinuddin A
- USN: 24BTRAO026
- Section: A
- Subject: Automation in Software Development