#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 14:00:14 2024

@author: mxu2
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 13:28:34 2024

@author: mxu2
"""

import pandas as pd
import numpy as np
import argparse
from calculate_modified_period import calculate_modified_period  # Import the calculate_modified_period function
from rankiteo_industry_mapping import map_to_category  # Import the map_to_category function
from prob_factors import adjust_probability  # Import adjustment factors for probabilities
from severity_function import predict_glm_severity_with_intervals, predict_probabilities  # Import the severity and probability prediction functions
from cost_mapping import calculate_total_cost  # Import the cost calculation functions

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

    # Map the sector to the predefined categories
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
        rf_prob = predict_probabilities('random_forest_model.pkl', input_data_rf)
        lr_prob = predict_probabilities('logistic_regression_model.pkl', input_data_lr)

        # Combine the probabilities (average)
        combined_prob = (rf_prob[0] + lr_prob[0]) / 2

        # Predict severity using the GLM model with intervals, quantiles, and Expected Shortfall
        severity, prediction_interval_95, quantile_99, es_95, es_99, quantile_95 = predict_glm_severity_with_intervals('itrc_glm1_model.pkl', input_data_glm)

        # Adjust the probability using the adjust_probability function
        adjusted_prob = adjust_probability(combined_prob, revenue, args.security_score, employees, followers)

        # Calculate costs based on severity, 99% quantile, and Expected Shortfall at 95% and 99% levels
        cost_based_on_severity = calculate_total_cost(mapped_sector, severity[0])
        cost_based_on_quantile_95 = calculate_total_cost(mapped_sector, quantile_95[0])
        cost_based_on_quantile_99 = calculate_total_cost(mapped_sector, quantile_99[0])
        cost_based_on_es_95 = calculate_total_cost(mapped_sector, es_95[0])
        cost_based_on_es_99 = calculate_total_cost(mapped_sector, es_99[0])

        # Calculate costs based on the prediction intervals
        cost_based_on_lower_bound_95 = calculate_total_cost(mapped_sector, prediction_interval_95[0][0])
        cost_based_on_upper_bound_95 = calculate_total_cost(mapped_sector, prediction_interval_95[1][0])

        # Print out the results for each breach type
        print(f"Breach Type: {breach_type}")
        print(f"Adjusted Probability: {adjusted_prob:.4f}")
        print(f"Predicted Severity: {severity[0]:,.0f} records")
        print(f"Cost Based on Severity: ${cost_based_on_severity:,.2f}")
        print(f"95% Prediction Interval: [{prediction_interval_95[0][0]:,.0f}, {prediction_interval_95[1][0]:,.0f}] records")
        print(f"Cost Based on 95% Interval Lower Bound: ${cost_based_on_lower_bound_95:,.2f}")
        print(f"Cost Based on 95% Interval Upper Bound: ${cost_based_on_upper_bound_95:,.2f}")
        print(f"Cost Based on 95% Quantile: ${cost_based_on_quantile_95:,.2f}")
        print(f"Cost Based on 99% Quantile: ${cost_based_on_quantile_99:,.2f}")
        print(f"Cost Based on ES 95%: ${cost_based_on_es_95:,.2f}")
        print(f"Cost Based on ES 99%: ${cost_based_on_es_99:,.2f}")
        print("="*50)

        # Append the results to the list
        results.append({
            'Type': breach_type,
            'Adjusted Probability': adjusted_prob,
            'Predicted Severity': severity[0],
            'Cost Based on Severity': cost_based_on_severity,
            'Cost Based on 95% Interval Lower Bound': cost_based_on_lower_bound_95,
            'Cost Based on 95% Interval Upper Bound': cost_based_on_upper_bound_95,
            'Cost Based on 95% Quantile': cost_based_on_quantile_95,
            'Cost Based on 99% Quantile': cost_based_on_quantile_99,
            'Cost Based on ES 95%': cost_based_on_es_95,
            'Cost Based on ES 99%': cost_based_on_es_99
        })

    # Convert results to a DataFrame and save to CSV
    results_df = pd.DataFrame(results)
    results_df.to_csv('breach_severity_predictions.csv', index=False)

    print("Results have been saved to breach_severity_predictions.csv")