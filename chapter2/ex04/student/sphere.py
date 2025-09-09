"""
Program: sphere.py
Author: Ziynet Akca

This program calculates the diameter, circumference, surface area, and volume of a sphere.
It prompts the user for the radius of the sphere (float) and computes these values using standard formulas.

Analysis:
- User inputs:
    - Radius of the sphere (floating-point number)
- Formulas used:
    - Diameter = 2 * radius
    - Circumference = 2 * pi * radius
    - Surface area = 4 * pi * radius^2
    - Volume = (4/3) * pi * radius^3
- Output: diameter, circumference, surface area, volume

Design (pseudocode):
1. Prompt user to enter radius (float)
2. Compute diameter = 2 * radius
3. Compute circumference = 2 * pi * radius
4. Compute surface area = 4 * pi * radius^2
5. Compute volume = (4/3) * pi * radius^3
6. Display all four values clearly labeled
"""
import math

# Request the radius
radius = float(input("Enter the radius of the sphere: "))

# Compute values
diameter = 2 * radius
circumference = 2 * math.pi * radius
surface_area = 4 * math.pi * radius**2
volume = (4/3) * math.pi * radius**3

# Display results
print("Diameter:", diameter)
print("Circumference:", circumference)
print("Surface area:", surface_area)
print("Volume:", volume)
