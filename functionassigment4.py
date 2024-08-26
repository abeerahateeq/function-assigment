# Function to calculate age
def calculate_age(birth_year, current_year):
    return current_year - birth_year

# Function to calculate area of rectangle
def area_of_rectangle(length, width):
    return length * width

# Function to calculate area of circle
def area_of_circle(radius):
    import math
    return math.pi * (radius ** 2)

# Function to calculate surface area of cube
def area_of_cube(side_length):
    return 6 * (side_length ** 2)

# Function to convert seconds into minutes and seconds
def convert_seconds(total_seconds):
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    return minutes, seconds

# Function to calculate percentage
def calculate_percentage(part, whole):
    return (part / whole) * 100

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

# Example usage:

# Age calculation
print("Your age is:", calculate_age(2007, 2024))

# Area of rectangle
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
print("The area of the rectangle is:", area_of_rectangle(length, width))

# Area of circle
radius = float(input("Enter the radius of the circle: "))
print("The area of the circle is:", area_of_circle(radius))

# Area of cube
side_length = float(input("Enter the side length of the cube: "))
print("The surface area of the cube is:", area_of_cube(side_length))

# Time units conversion
minutes, seconds = convert_seconds(200)
print("Minutes:", minutes)
print("Seconds:", seconds)

# Calculating percentage
numerator = float(input("Enter the part: "))
denominator = float(input("Enter the whole: "))
print("Percentage:", calculate_percentage(numerator, denominator), "%")

# Temperature unit conversion
fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = fahrenheit_to_celsius(fahrenheit)
print(f"{fahrenheit:.2f}°F is equivalent to {celsius:.2f}°C")

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius:.2f}°C is equivalent to {fahrenheit:.2f}°F")
