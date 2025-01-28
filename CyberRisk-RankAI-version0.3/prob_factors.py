import math

def adjust_probability(prob, revenue, security_score, employees, followers):
    # Ensure revenue is either a float or None
    if isinstance(revenue, str) and revenue.lower() == "unknown":
        revenue = None
    else:
        try:
            revenue = float(revenue)
        except (TypeError, ValueError):
            revenue = None

    # Ensure employees is either an int or None
    if isinstance(employees, str) and employees.lower() == "unknown":
        employees = None
    else:
        try:
            employees = int(employees)
        except (TypeError, ValueError):
            employees = None

    # Ensure followers is either an int or None
    if isinstance(followers, str) and followers.lower() == "unknown":
        followers = None
    else:
        try:
            followers = int(followers)
        except (TypeError, ValueError):
            followers = None

    # Revenue adjustment
    if revenue is not None and revenue > 0:
        if revenue <= 50000000:
            prob *= (1 + 0.213)
        elif 50000000 < revenue <= 300000000:
            prob *= (1 + 0.0855)
        elif 300000000 < revenue <= 2000000000:
            prob *= (1 + 0.0235)
        elif 2000000000 < revenue <= 10000000000:
            prob *= (1 + 0.0065)
        elif 10000000000 < revenue <= 100000000000:
            prob *= (1 + 0.0025)
        elif revenue > 100000000000:
            prob *= (1 + 0.0005)
    else:  # Unknown or None revenue
        prob *= (1 + 0.169)

    # Security score adjustment
        prob *= (math.exp(1 - security_score / 1000) / 1.22)

    # Employee adjustment (only if revenue is unknown)
    if revenue is None:
        if employees is None or employees <= 0:
            prob *= (1 + 0.005)
        elif employees <= 100:
            prob *= (1 + 0.005)
        elif 100 < employees <= 1000:
            prob *= (1 + 0.01)
        elif 1000 < employees <= 10000:
            prob *= (1 + 0.02)
        elif 10000 < employees <= 100000:
            prob *= (1 + 0.03)
        elif employees > 100000:
            prob *= (1 + 0.05)

    # Followers adjustment (only if revenue and employees are unknown)
    if revenue is None and (employees is None or employees <= 0):
        if followers is not None and followers > 100000:
            prob *= (1 + 0.02)

    return prob
