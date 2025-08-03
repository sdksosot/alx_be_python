def safe_divide(numerator:float, denominator:float):
    try:
        return float(numerator) /float(denominator) 
    except ZeroDivisionError:
       return "Error: Cannot divide by zero."
    except ValueError:
        return 'value error'

