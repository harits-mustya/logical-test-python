# Quiz 16: Temperature Converter
# Write a function celsius_to_fahrenheit(c) that converts a temperature from Celsius to Fahrenheit.

# Example:
# python
# celsius_to_fahrenheit(0)   # 32.0
# celsius_to_fahrenheit(100) # 212.0

def celsius_to_fahrenheit(n):
    fahrenheit = (9/5) * n + 32

    print(fahrenheit)
    return fahrenheit

celsius_to_fahrenheit(100)