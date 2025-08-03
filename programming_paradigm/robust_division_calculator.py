def safe_divide(numerator, denominator):
    """
    Safely divides two numbers with comprehensive error handling
    
    Args:
        numerator: Number to be divided
        denominator: Number to divide by
        
    Returns:
        str: Result message or error message
    """
    try:
        num = float(numerator)
        den = float(denominator)
    except ValueError:
        return "Error: Both arguments must be numeric values"
    
    try:
        result = num / den
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."


