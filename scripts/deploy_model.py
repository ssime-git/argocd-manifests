import joblib
import os

def deploy_model():
    # In a real-world scenario, this script would handle the deployment
    # of the model to a production environment. For this example, we'll
    # simply copy the model to a "deployment" directory.
    
    # Create deployment directory if it doesn't exist
    os.makedirs('/app/deployment', exist_ok=True)
    
    # Copy the model to the deployment directory
    joblib.dump(joblib.load('/app/model/iris_model.joblib'), '/app/deployment/iris_model_prod.joblib')

if __name__ == "__main__":
    deploy_model()
    print("Model deployment completed.")