def safe_divide(numerator:float, denominator:float):
    try:
        num = float(numerator)
        dem = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."  
    try:
       resulte =  num / dem  
    except ZeroDivisionError:
       return "Error: Cannot divide by zero."
    return f"The result of the division is {result}"

