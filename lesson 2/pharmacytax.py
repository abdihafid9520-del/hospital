def calculate_tax(amount):
    """Apply 5% tax to bills of 1,000 or more."""
    if amount >= 1000:
        return amount * 0.05
    return 0
