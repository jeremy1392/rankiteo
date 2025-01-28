#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Version 0.2 - RiskSphere AI
"""

import pandas as pd
import numpy as np
import argparse
from prob_factors import adjust_probability  # Import adjustment factors for probabilities
from calculate_modified_period import calculate_modified_period  # Import the calculate_modified_period function
from rankiteo_industry_mapping import map_to_category  # Import the map_to_category function
from severity_function import predict_glm_severity_with_intervals, predict_probabilities 

# List of breach types to evaluate
breach_types = ['Cyberattack', 'Humansystemerror', 'Physicalattack']

# Main script
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Predict probabilities and severity using pretrained models.')
    parser.add_argument('--sector', type=str, help='Sector of the business.', default="finance")
    parser.add_argument('--policy_length', type=int, choices=[6, 12], help='Policy length in months (6 or 12).', default=12)
    parser.add_argument('--security_score', type=float, help='Security score as an input feature.', default=350.0)
    parser.add_argument('--revenue', type=str, help='Revenue of the business (provide number or "Unknown").', default="Unknown")
    parser.add_argument('--employees', type=str, help='Number of employees in the business (provide number or "Unknown").', default="Unknown")
    parser.add_argument('--followers', type=str, help='Number of followers on social media (provide number or "Unknown").', default="Unknown")
    args = parser.parse_args()

    # Map the sector to predefined categories
    mapped_sector = map_to_category(args.sector)

    # Calculate the modified period based on policy length
    modified_period = calculate_modified_period(args.policy_length)
    modified_period_discrete = np.floor(modified_period).astype(int)

    # Prepare input data that remains constant for all breach types
    input_data_lr = {
        'Modified_Period': [modified_period],
        'Sector': [mapped_sector]
    }

    input_data_rf = {
        'Modified_Period_Discrete': [modified_period_discrete],
        'Sector': [mapped_sector]
    }

    input_data_glm = {
        'Modified_Period_poly1': [modified_period],
        'Modified_Period_poly2': [modified_period**2],
        'Sector': [mapped_sector]
    }


    # Convert revenue, employees, and followers to appropriate types
    revenue = None if isinstance(args.revenue, str) and args.revenue.lower() == "unknown" else float(args.revenue)
    employees = None if isinstance(args.employees, str) and args.employees.lower() == "unknown" else int(args.employees)
    followers = None if isinstance(args.followers, str) and args.followers.lower() == "unknown" else int(args.followers)

    # Prepare to collect results
    results = []

    # Loop through each breach type
    for breach_type in breach_types:
        # Update only the type in the input data
        input_data_lr['Type'] = [breach_type]
        input_data_rf['Type'] = [breach_type]
        input_data_glm['Type'] = [breach_type]

        # Predict probabilities using both models
        rf_prob = predict_probabilities('model1.pkl', input_data_rf)
        lr_prob = predict_probabilities('model2.pkl', input_data_lr)

        # Combine the probabilities (average)
        combined_prob = (rf_prob[0] + lr_prob[0]) / 2

        # Predict severity using the GLM model with intervals
        severity, prediction_interval_95, quantile_99, es_95, es_99, quantile_95 = predict_glm_severity_with_intervals(
            'model3.pkl', input_data_glm
        )

        # Adjust the probability using the adjust_probability function
        adjusted_prob = adjust_probability(combined_prob, revenue, args.security_score, employees, followers)
        
        # Change 'Physicalattack' to 'Others' in the output
        output_type = "Others" if breach_type == "Physicalattack" else breach_type

        # Print results
        print(f"Breach Type: {output_type}")
        print(f"Adjusted Probability: {adjusted_prob:.4f}")
        print(f"Predicted Severity: {severity.iloc[0]:,.0f} records")
        print(f"95% Prediction Interval: [{prediction_interval_95[0][0]:,.0f}, {prediction_interval_95[1][0]:,.0f}] records")
        print(f"99% Quantile Severity: {quantile_99.iloc[0]:,.0f} records")
        print(f"Expected Shortfall (95%): {es_95.iloc[0]:,.0f} records")
        print(f"Expected Shortfall (99%): {es_99.iloc[0]:,.0f} records")
        print("=" * 50)

        # Append results
        results.append({
            'Type': output_type,
            'Adjusted Probability': adjusted_prob,
            'Predicted Severity': severity.iloc[0],
            '95% Prediction Interval': f"[{prediction_interval_95[0][0]:,.0f}, {prediction_interval_95[1][0]:,.0f}]",
            '99% Quantile': quantile_99.iloc[0],
            'ES 95%': es_95.iloc[0],
            'ES 99%': es_99.iloc[0]
        })

    # Save results to a CSV file
    results_df = pd.DataFrame(results)
    results_df.to_csv('quantifyedge_predictions.csv', index=False)