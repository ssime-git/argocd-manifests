import pandas as pd
from sklearn.datasets import load_iris

def ingest_data():
    # Load the Iris dataset
    iris = load_iris()
    
    # Create a DataFrame
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['target'] = iris.target
    
    # Save the data
    df.to_csv('/app/data/iris_data.csv', index=False)

if __name__ == "__main__":
    ingest_data()
    print("Data ingestion completed.")