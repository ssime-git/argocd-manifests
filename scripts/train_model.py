import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

def train_model():
    # Load preprocessed data
    X_train = pd.read_csv('/app/data/X_train.csv')
    y_train = pd.read_csv('/app/data/y_train.csv')
    
    # Train the model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train.values.ravel())
    
    # Save the model
    joblib.dump(model, '/app/model/iris_model.joblib')

if __name__ == "__main__":
    train_model()
    print("Model training completed.")