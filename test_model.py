from modules.predictor import predict_resume

sample_resume = """
Python Developer with experience in Python, Java,
SQL, Django, Flask, REST APIs and MySQL.
Developed web applications and backend services.
Knowledge of data structures, algorithms,
machine learning and software development.
"""

results = predict_resume(sample_resume)

print("\nTop 3 Job Predictions:\n")

for result in results:
    print(result["category"], "-", result["confidence"], "%")