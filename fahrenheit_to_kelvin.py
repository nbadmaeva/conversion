# Conversion Fahrenheit to Kelvin
# Formula: K = (F - 32)/ 1.8 + 273.15

def fahrenheit_to_kelvin(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius + 273.15 

print fahrenheit_to_kelvin(1)