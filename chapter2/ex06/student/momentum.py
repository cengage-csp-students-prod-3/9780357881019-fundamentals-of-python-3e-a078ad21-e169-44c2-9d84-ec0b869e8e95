"""
Program: momentum.py
Author: Ziynet Akca

This program calculates the object's momentum and kinetic energy.

ANALYSIS
The user provides 2 inputs (mass and velocity).
The program computes:
- Momentum by using the formula: Momentum = mass * velocity
- Kinetic energy by using the formula: KE = (1/2) * m * v^2

DESIGN
1. Prompt the user for the object's mass.
2. Prompt the user for the object's velocity.
3. Calculate momentum with the formula Momentum = mass * velocity.
4. Calculate kinetic energy with the formula KE = 0.5 * mass * velocity^2.
5. Display both results clearly.
"""


mass = float(input("Enter the object's mass (kg): "))
velocity = float(input("Enter the object's velocity (m/s): "))


momentum = mass * velocity
KE = 0.5 * mass * (velocity ** 2)


print("The object's momentum is", momentum)
print("The object's kinetic energy is", KE)
