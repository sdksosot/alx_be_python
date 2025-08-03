def safe_divide(numerator, denominator):
    """
    Safely divides two numbers with comprehensive error handling
    
    Args:
        numerator: Number to be divided
        denominator: Number to divide by
        
    Returns:
        float: Result of division if successful
        str: Error message if division fails
    """
    try:
        num = float(numerator)
        den = float(denominator)
    except ValueError:
        return "Error: Both arguments must be numeric values"
    
    try:
        result = num / den
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    
    return f"The result of the division is {result}"



