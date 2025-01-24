#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 13:58:54 2024

@author: mxu2
"""

# cost_mapping.py

# Cost per record by sector
cost_per_record = {
    "Financial Services": 315,
    "Professional Services": 230,
    "Healthcare": 496,
    "Manufacturing": 217,
    "Education": 180,
    "Government": 240,
    "Retail": 180,
    "Technology": 230,
    "Non-Profit/NGO": 190,
    "Hospitality": 180,
    "Transportation": 217,
    "Mining/Construction": 217,
    "Utilities": 217,
    "Social Services": 190,
    "Wholesale Trade": 180,
    "HR/Staffing": 230,
    "Other": 230
}

# Category mapping
categories = {
    "Financial Services": ["Financial Services", "Banking", "Insurance", "Investment Management"],
    "Professional Services": ["Professional Services", "Law Practice", "Accounting", "Consulting", "Legal Services", "Business Consulting and Services"],
    "Healthcare": ["Healthcare", "Hospitals and Health Care", "Medical Practices", "Pharmaceutical Manufacturing", "Biotechnology Research", "Mental Health Care", "Medical Equipment Manufacturing"],
    "Manufacturing": ["Manufacturing", "Motor Vehicle Manufacturing", "Machinery Manufacturing", "Computers and Electronics Manufacturing", "Industrial Machinery Manufacturing", "Chemical Manufacturing", "Textile Manufacturing", "Food and Beverage Manufacturing", "Fabricated Metal Products", "Printing Services", "Semiconductor Manufacturing"],
    "Education": ["Education", "Higher Education", "Primary and Secondary Education", "Education Administration Programs", "Education Management"],
    "Government": ["Government", "Government Administration", "Public Policy Offices", "Military", "Armed Forces"],
    "Retail": ["Retail", "Retail Office Equipment", "Retail Art Supplies", "Retail Health and Personal Care Products", "Retail Apparel and Fashion", "Retail Luxury Goods and Jewelry"],
    "Technology": ["Technology", "IT Services and IT Consulting", "Software Development", "Computer and Network Security", "Computer Hardware Manufacturing", "Telecommunications"],
    "Non-Profit/NGO": ["Non-Profit/NGO", "Non-profit Organizations", "Non-profit Organization Management", "Civic and Social Organizations", "Social Services"],
    "Hospitality": ["Hospitality", "Food & Beverages", "Food and Beverage Services", "Restaurants", "Entertainment Providers", "Hospitality Services"],
    "Transportation": ["Transportation", "Rail Transportation", "Truck Transportation", "Airlines and Aviation", "Ground Passenger Transportation", "Freight and Package Transportation"],
    "Mining/Construction": ["Mining/Construction", "Mining", "Construction", "Building Materials", "Wholesale Building Materials", "Civil Engineering"],
    "Utilities": ["Utilities", "Solar Electric Power Generation", "Utilities"],
    "Social Services": ["Social Services", "Individual and Family Services", "Religious Institutions", "Civic and Social Organizations", "Fundraising", "HR/Staffing", "Human Resources Services"],
    "Wholesale Trade": ["Wholesale Trade", "Wholesale", "Wholesale Building Materials", "Wholesale Food and Beverages"],
    "HR/Staffing": ["HR/Staffing", "Staffing and Recruiting", "Human Resources Services"],
    "Other": ["Other", "NA", "Unknown", "Miscellaneous"]
}

# Function to get the cost per record based on the sector
def get_cost_per_record(sector):
    for category, sectors in categories.items():
        if sector in sectors:
            return cost_per_record[category]
    return cost_per_record["Other"]  # Default to "Other" if sector not found

# Function to calculate total cost based on severity
def calculate_total_cost(sector, severity):
    cost_per_record = get_cost_per_record(sector)
    total_cost = severity * cost_per_record
    return total_cost
