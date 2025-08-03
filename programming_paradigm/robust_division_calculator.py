def safe_divide(numerator, denominator):
    try:
        return numerator / denominator
    except ZeroDivisionError:
       return 'you cant devide by zero '
    except ValueError:
        return 'value error'