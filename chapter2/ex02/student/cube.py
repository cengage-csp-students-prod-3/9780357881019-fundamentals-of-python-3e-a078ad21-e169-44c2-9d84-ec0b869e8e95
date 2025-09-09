"""
Program: cube_surface_area.py
Author: Ziynet Akca

This program calculates the surface area of a cube.

Analysis:
- The user provides the length of the cube's edge.
- The program uses the formula: surface area = 6 * edge^2
- The program displays the surface area with a descriptive message.

Design (pseudocode):
1. Prompt the user to enter the cube's edge length.
2. Read the edge length as a floating-point number.
3. Compute the surface area using the formula: 6 * edge^2
4. Display the result with an appropriate message.
"""


edge = float(input("Enter the cube's edge: "))
surfaceArea = 6 * edge**2
print("The surface area is", surfaceArea, "square units.")
