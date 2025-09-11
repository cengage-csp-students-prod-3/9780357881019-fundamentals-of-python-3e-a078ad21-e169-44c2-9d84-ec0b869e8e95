"""
Program: momentum.py
Author: Ziynet Akca

This program calculates the momentum of an object.

Analysis:
- The user provides two inputs: 
  1. mass (in kilograms)
  2. velocity (in meters per second)
- The program computes the momentum using the formula:
      momentum = mass * velocity

Design (pseudocode):
1. Prompt the user for the object's mass (kg).
2. Prompt the user for the object's velocity (m/s).
3. Compute the momentum = mass * velocity.
4. Display the result with appropriate labeling.
"""

# Request inputs
mass = float(input("Enter the object's mass in kilograms: "))
velocity = float(input("Enter the object's velocity in meters per second: "))

# Compute momentum
momentum = mass * velocity

# Display output
print("The momentum is", momentum, "kg·m/s")
