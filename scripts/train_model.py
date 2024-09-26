import numpy as np
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

def train_model():
    print("Starting model training...")
    # Load preprocessed data
    data = np.load('/app/data/preprocessed_data.npz')
    X_train, y_train = data['X_train'], data['y_train']
    
    # Train the model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Save the model
    os.makedirs('/app/model', exist_ok=True)
    joblib.dump(model, '/app/model/iris_model.joblib')
    print("Model saved to /app/model/iris_model.joblib")

if __name__ == "__main__":
    train_model()
    print("Model training completed.")