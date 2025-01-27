#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Version 0.1 - StatGuard AI
"""

import pandas as pd
import argparse
from calculate_modified_period import calculate_modified_period
from rankiteo_industry_mapping import map_to_category
import pickle
import math

 
with open('glm.pkl', 'rb') as f:
    glm_model = pickle.load(f)

# Load the label encoders
with open('label_encoders.pkl', 'rb') as f:
    label_encoders = pickle.load(f)


# List of breach types to evaluate
breach_types = ['Cyberattack', 'Humansystemerror', 'Physicalattack']

# Main script
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Predict breach probabilities using the logistic regression model.')
    parser.add_argument('--sector', type=str, required=True, help='Sector of the business (e.g., Finance, Education, Healthcare).')
    parser.add_argument('--policy_length', type=int, choices=[6, 12], required=True, help='Policy length in months (6 or 12).')
    parser.add_argument('--security_score', type=float, required=True, help='Security score (e.g., 350-1000 scale).')
    args = parser.parse_args()

    # Map the sector to a predefined category
    mapped_sector = map_to_category(args.sector)
    
    # Calculate the modified period based on the policy length
    modified_period = calculate_modified_period(args.policy_length)

    # Prepare input data for the logistic regression model
    input_data_lr = {
        'Modified_Period': [modified_period],
        'Sector': [mapped_sector]
    }

    # Prepare to collect results
    results = []

    # Loop through each breach type
    for breach_type in breach_types:
        # Add breach type to input data
        input_data_lr['Type'] = [breach_type]

        # Prepare input data for logistic regression (X_lr)
        X_lr = pd.DataFrame(input_data_lr)[['Modified_Period', 'Sector', 'Type']]
        
        # Encode categorical features for logistic regression
        for feature in ['Sector', 'Type']:
            if feature in label_encoders:
                X_lr[feature] = label_encoders[feature].transform(X_lr[feature].fillna('Unknown'))
        
        # Predict probabilities 
        lr_prob = glm_model.predict_proba(X_lr)[:, 1]
      
        adjusted_prob = lr_prob[0]*(math.exp(1 - args.security_score / 1000) / 1.22)
        # Print out the results for each breach type
        print(f"Breach Type: {breach_type}")
        print(f"Adjusted Probability: {adjusted_prob:.4f}")
        print("=" * 50)

        # Append the results to the list
        results.append({
            'Type': breach_type,
            'Adjusted Probability': adjusted_prob
        })

    # Convert results to a DataFrame and save to CSV
    results_df = pd.DataFrame(results)
    results_df.to_csv('breach_probability_predictions.csv', index=False)

    print("Results have been saved to breach_probability_predictions.csv")
