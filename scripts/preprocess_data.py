import pandas as pd
from sklearn.model_selection import train_test_split
import os
import sys

def preprocess_data():
    print("Starting preprocessing...")
    print(f"Current working directory: {os.getcwd()}")
    print(f"Contents of current directory: {os.listdir('.')}")
    print(f"Contents of /app: {os.listdir('/app')}")
    print(f"Contents of /app/data: {os.listdir('/app/data')}")
    
    file_path = '/app/data/iris_data.csv'
    print(f"Attempting to read file: {file_path}")
    
    if not os.path.exists(file_path):
        print(f"Error: File {file_path} does not exist!")
        sys.exit(1)
    
    try:
        df = pd.read_csv(file_path)
        print(f"Successfully loaded data. Shape: {df.shape}")
        print(f"Column names: {df.columns.tolist()}")
        print(f"First few rows:\n{df.head()}")
    except Exception as e:
        print(f"Error reading CSV file: {str(e)}")
        sys.exit(1)
    
    # Split features and target
    X = df.drop('target', axis=1)
    y = df['target']
    
    # Split into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Save preprocessed data
    X_train.to_csv('/app/data/X_train.csv', index=False)
    X_test.to_csv('/app/data/X_test.csv', index=False)
    y_train.to_csv('/app/data/y_train.csv', index=False)
    y_test.to_csv('/app/data/y_test.csv', index=False)
    
    print("Preprocessing completed. Files saved in /app/data/")
    print(f"Final contents of /app/data: {os.listdir('/app/data')}")

if __name__ == "__main__":
    preprocess_data()
    print("Data preprocessing completed.")