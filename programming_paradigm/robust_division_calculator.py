def safe_divide(numerator:float, denominator:float):
    try:
        return float(numerator) /float(denominator) 
    except ZeroDivisionError:
       return 'you cant devide by zero '
    except ValueError:
        return 'value error'
