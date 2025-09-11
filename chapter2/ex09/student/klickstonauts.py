"""
Program: klickstonauts.py
Author: Ziynet Akca

This program converts a given distance in kilometers to nautical miles.

ANALYSIS
- 1 kilometer represents 1/10,000 of the distance from the North Pole to the equator.
- From the North Pole to the equator there are 90 degrees.
- Each degree has 60 minutes of arc.
- A nautical mile equals 1 minute of arc.

So:
1 degree = 60 nautical miles
90 degrees = 90 * 60 = 5400 nautical miles
10,000 km = 5400 nautical miles
1 km = 5400 / 10,000 = 0.54 nautical miles

DESIGN
1. Prompt the user for a distance in kilometers.
2. Multiply the input value by 0.54 to get the equivalent nautical miles.
3. Display the result.
"""

# Step 1: input
kilometers = float(input("Enter the number of kilometers: "))

# Step 2: conversion factor
nautical_miles = kilometers * 0.54

# Step 3: output
print("The number of nautical miles is", round(nautical_miles, 2))
