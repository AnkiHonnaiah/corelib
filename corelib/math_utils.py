def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def calc_discount(price, percentage):
    """Calculate discounted price"""
    return price - (price * percentage / 100.0)

def apply_discount(price, percentage):
    """Apply discount in a precise way"""
    return round(price - (price * percentage / 100.0), 2)
