FAHRENHEIT_TO_CELSIUS_FACTOR = float(input("Enter the temperature to convert: "))
f_c = input('Is this temperature in Celsius or Fahrenheit? (C/F): ').lower()
def convert_to_celsius(fahrenheit):
    return  (fahrenheit - 32) * (5/9)
def convert_to_fahrenheit(celsius):
    return  (celsius * (9/5)) + 32
if f_c == 'c':
    print(f'{FAHRENHEIT_TO_CELSIUS_FACTOR}°F is {convert_to_celsius(FAHRENHEIT_TO_CELSIUS_FACTOR)}°C')
elif f_c == 'f':
    print(f'{FAHRENHEIT_TO_CELSIUS_FACTOR}°C is {convert_to_fahrenheit(FAHRENHEIT_TO_CELSIUS_FACTOR)}°F')
else:
    print("invalid temperature. Please enter a numeric value")
