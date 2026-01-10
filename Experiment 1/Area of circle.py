#Method 1
radius_input = input("Enter the radius: ")
radius = float(radius_input)

pi = 3.14
area = pi * radius * radius

#Display result
print("The area of the circle with radius", radius, "is", area)

#Method 2
import math
radius = float(input("Enter Radius of circle: "))
area = 3.14 * (radius ** 2)

#f is format activator for using the curly brackets as place holder and variable with in it
print(f"The area of circle with radius {radius} is: {area:.4f}")
