import pandas as pd
from sklearn.model_selection import train_test_split

def preprocess_data():
    # Load the data
    df = pd.read_csv('/app/data/iris_data.csv')
    
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

if __name__ == "__main__":
    preprocess_data()
    print("Data preprocessing completed.")