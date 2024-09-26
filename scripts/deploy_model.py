import joblib
import os
import shutil

def deploy_model():
    print("Starting model deployment...")
    # Create deployment directory
    os.makedirs('/app/deployment', exist_ok=True)
    
    # Copy the model to the deployment directory
    shutil.copy('/app/model/iris_model.joblib', '/app/deployment/iris_model_prod.joblib')
    
    print("Model deployed to /app/deployment/iris_model_prod.joblib")
    
    # Print evaluation results
    with open('/app/results/evaluation.txt', 'r') as f:
        print("Evaluation results:")
        print(f.read())

if __name__ == "__main__":
    deploy_model()
    print("Model deployment completed.")