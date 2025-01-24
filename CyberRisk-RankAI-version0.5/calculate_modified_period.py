#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 13:56:00 2024

@author: mxu2
"""

# calculate_modified_period.py

from datetime import datetime, timedelta

def calculate_modified_period(policy_length_months, base_period=11, base_date='2024-06-30'):
    """
    Calculates the modified period based on the policy length.

    Parameters:
    policy_length_months (int): The policy length in months (e.g., 6 or 12).
    base_period (int): The base period (e.g., 11 for the end date of 2024-06-30).
    base_date (str): The base date in 'YYYY-MM-DD' format (default is '2024-06-30').

    Returns:
    float: The modified period as a float number.
    """
    today = datetime.today()
    end_date = today + timedelta(days=(policy_length_months * 30))  # Approximation for months
    base_date = datetime.strptime(base_date, '%Y-%m-%d')
    
    # Calculate the difference in months from the base date
    diff_months = (end_date.year - base_date.year) * 12 + end_date.month - base_date.month
    
    # Determine the modified period
    modified_period = base_period + diff_months / 6
    return modified_period
