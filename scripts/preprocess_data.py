import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import os

def preprocess_data():
    print("Starting preprocessing...")
    print(f"Contents of /app/data: {os.listdir('/app/data')}")
    
    # Load the data
    df = pd.read_csv('/app/data/iris_data.csv')
    print(f"Loaded data shape: {df.shape}")
    
    # Split features and target
    X = df.drop('target', axis=1)
    y = df['target']
    
    # Split into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Save preprocessed data
    np.savez('/app/data/preprocessed_data.npz', X_train=X_train, X_test=X_test, y_train=y_train, y_test=y_test)
    print("Preprocessing completed. Data saved to /app/data/preprocessed_data.npz")

if __name__ == "__main__":
    preprocess_data()