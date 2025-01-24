import pandas as pd
import numpy as np
import pickle
from scipy.stats import norm

def predict_glm_severity_with_intervals(model_file, input_data):
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

    # Calculate the 95% prediction interval
    z_95 = norm.ppf(0.975)
    lower_bound_95 = np.exp(log_severity - z_95 * se_log_severity)
    upper_bound_95 = np.exp(log_severity + z_95 * se_log_severity)
    
    # Calculate the 95% quantile
    z1_95 = norm.ppf(0.95)
    quantile_95 = np.exp(log_severity + z1_95 * se_log_severity)

    # Calculate the 99% quantile
    z_99 = norm.ppf(0.99)
    quantile_99 = np.exp(log_severity + z_99 * se_log_severity)

    # Calculate Expected Shortfall (ES) at the 95% level
    es_95 = np.exp(log_severity + se_log_severity**2 / 2) * norm.pdf(z_95) / (1 - 0.95)

    # Calculate Expected Shortfall (ES) at the 99% level
    es_99 = np.exp(log_severity + se_log_severity**2 / 2) * norm.pdf(z_99) / (1 - 0.99)

    return adjusted_severity, (lower_bound_95, upper_bound_95), quantile_99, es_95, es_99, quantile_95



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
