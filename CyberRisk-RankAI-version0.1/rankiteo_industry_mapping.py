import difflib

# Define the mapping categories
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
    "Other": ["Other", "NA", "Unknown", "Miscellaneous"],
}

def map_to_category(sector):
    # Check for exact match or partial match within the sectors
    for category, industry_list in categories.items():
        if any(sector.lower() in industry.lower() for industry in industry_list):
            return category
    # If no match is found, use the closest match
    all_industries = [industry for sublist in categories.values() for industry in sublist]
    closest_match = difflib.get_close_matches(sector, all_industries, n=1)
    if closest_match:
        for category, industry_list in categories.items():
            if closest_match[0] in industry_list:
                return category
    return "Other"
