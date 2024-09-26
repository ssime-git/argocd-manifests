import pandas as pd
import joblib
from sklearn.metrics import accuracy_score, classification_report

def evaluate_model():
    # Load the model
    model = joblib.load('/app/model/iris_model.joblib')
    
    # Load test data
    X_test = pd.read_csv('/app/data/X_test.csv')
    y_test = pd.read_csv('/app/data/y_test.csv')
    
    # Make predictions
    y_pred = model.predict(X_test)
    
    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)
    
    # Generate classification report
    report = classification_report(y_test, y_pred)
    
    # Save evaluation results
    with open('/app/results/evaluation.txt', 'w') as f:
        f.write(f"Accuracy: {accuracy}\n\n")
        f.write("Classification Report:\n")
        f.write(report)

if __name__ == "__main__":
    evaluate_model()
    print("Model evaluation completed.")