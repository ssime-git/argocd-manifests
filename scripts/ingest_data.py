import pandas as pd
from sklearn.datasets import load_iris
import os

def ingest_data():
    print(f"Current working directory: {os.getcwd()}")
    print(f"Contents of current directory: {os.listdir('.')}")
    print(f"Contents of /app: {os.listdir('/app')}")
    
    # Load the Iris dataset
    iris = load_iris()
    
    # Create a DataFrame
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['target'] = iris.target
    
    # Ensure the directory exists
    os.makedirs('/app/data', exist_ok=True)
    
    # Save the data
    file_path = '/app/data/iris_data.csv'
    df.to_csv(file_path, index=False)
    print(f"Data saved to {os.path.abspath(file_path)}")
    print(f"Contents of /app/data: {os.listdir('/app/data')}")
    print(f"File size: {os.path.getsize(file_path)} bytes")

if __name__ == "__main__":
    ingest_data()
    print("Data ingestion completed.")