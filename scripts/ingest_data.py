import pandas as pd
from sklearn.datasets import load_iris
import os

def ingest_data():
    # Load the Iris dataset
    iris = load_iris()
    
    # Create a DataFrame
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['target'] = iris.target
    
    # Save the data
    os.makedirs('/app/data', exist_ok=True)
    df.to_csv('/app/data/iris_data.csv', index=False)
    print(f"Data saved to /app/data/iris_data.csv")

if __name__ == "__main__":
    ingest_data()
    print("Data ingestion completed.")