# asking user to inout a value in celcius.
celcius_written_value = float(input("Enter a value in Celcius: "))

# conversion calculation, c to f.
fahrenheit_conversion = (9 / 5) * celcius_written_value + 32

# making the conversion.
new_value = celcius_written_value + fahrenheit_conversion

# converted to f and showing results
print(f"{celcius_written_value} degrees C is {fahrenheit_conversion:.1f} degrees F")