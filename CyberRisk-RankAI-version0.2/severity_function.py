import pandas as pd
import numpy as np
import pickle
from scipy.stats import norm

def predict_glm_severity(model_file, input_data):
    # Load the GLM model
    with open(model_file, 'rb') as f:
        model = pickle.load(f)

    # Convert input data to a DataFrame
    X = pd.DataFrame(input_data)

    # Predict the log of severity (VictimsImpacted)
    log_severity = model.predict(X)

    # Check if the design matrix extraction is correct for your model
    design_matrix = model.model.exog  # Ensure this matches your model structure

    # Ensure the selected rows align correctly with the input data
    selected_design_matrix = design_matrix[:len(X)]  # Verify this alignment

    # Calculate the standard errors for predictions
    se_log_severity = np.sqrt(np.sum((selected_design_matrix @ model.cov_params().values) * selected_design_matrix, axis=1))

    # Bias correction for severity prediction
    adjusted_severity = np.exp(log_severity + (se_log_severity**2) / 2)

   
    return adjusted_severity



# Function to load the model and predict probabilities
def predict_probabilities(model_file, input_data, model_type='lr'):
    with open(model_file, 'rb') as f:
        model = pickle.load(f)

    X = pd.DataFrame(input_data)

    if model_type != 'glm':
        # Load and apply the encoder for categorical features
        with open('label_encoders.pkl', 'rb') as f:
            encoder = pickle.load(f)
        
        for feature in encoder:
            X[feature] = encoder[feature].transform(X[feature].fillna('Unknown'))
    
    # Predict probabilities or severity
    if model_type == 'glm':
        # For GLM, the prediction will be handled by a separate function
        raise NotImplementedError("Use the predict_glm_severity_with_intervals function for GLM predictions.")
    else:
        probabilities = model.predict_proba(X)[:, 1]  # Probability of the positive class
        return probabilities
