"""
Program: cube.py
Author: Ziynet Akca

Purpose:
Calculate the surface area of a cube given its edge length.

Analysis:
- Input: the user provides the length of the cube's edge.
- Computation: surface area = 6 * (edge^2)
- Output: display the surface area with units.

Design (pseudocode):
1. Prompt the user to enter the cube's edge length.
2. Read the input as a float.
3. Compute the surface area using the formula: 6 * edge^2.
4. Print the surface area with a descriptive message.
"""


edge = 5.0
surfaceArea = 6 * edge**2
print("The surface area is", surfaceArea, "square units.")



