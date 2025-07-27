FAHRENHEIT_TO_CELSIUS_FACTOR = (5/9)
CELSIUS_TO_FAHRENHEIT_FACTOR = (9/5) 

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

try:
    temp = float(input("Enter the temperature to convert: "))
    t_c = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").lower()
    
    if t_c == 'c':
        print(f'{temp}°C is {convert_to_fahrenheit(temp)}°F')
    elif t_c == 'f':
        print(f'{temp}°F is {convert_to_celsius(temp)}°C')
    else:
        print("Invalid unit. Please enter 'C' or 'F'.")
except ValueError:
    print("Invalid temperature. Please enter a numeric value.")
