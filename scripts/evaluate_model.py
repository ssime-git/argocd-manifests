import numpy as np
import joblib
from sklearn.metrics import accuracy_score, classification_report
import os

def evaluate_model():
    print("Starting model evaluation...")
    # Load the model
    model = joblib.load('/app/model/iris_model.joblib')
    
    # Load test data
    data = np.load('/app/data/preprocessed_data.npz')
    X_test, y_test = data['X_test'], data['y_test']
    
    # Make predictions
    y_pred = model.predict(X_test)
    
    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)
    
    # Generate classification report
    report = classification_report(y_test, y_pred)
    
    # Save evaluation results
    os.makedirs('/app/results', exist_ok=True)
    with open('/app/results/evaluation.txt', 'w') as f:
        f.write(f"Accuracy: {accuracy}\n\n")
        f.write("Classification Report:\n")
        f.write(report)
    
    print("Evaluation results saved to /app/results/evaluation.txt")

if __name__ == "__main__":
    evaluate_model()
    print("Model evaluation completed.")