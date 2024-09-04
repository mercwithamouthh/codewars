def calculate_years(P, I, T, D):
    years = 0
    while P < D:
        # Calculate the interest for this year
        interest = P * I
        # Calculate the tax on the interest
        tax = interest * T
        # Update the principal with the post-tax interest
        P += interest - tax
        # Increment the year count
        years += 1
    return years
