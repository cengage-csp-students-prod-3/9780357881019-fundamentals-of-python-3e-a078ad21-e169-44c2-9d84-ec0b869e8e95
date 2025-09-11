"""
Program: momentum.py
Author: Ziynet Akca

This program calculates the object`s kinetic energy.

ANALYSIS

The user provides 2 inputs(mass and velocity)
The program computes the object`s kinetic energy by using the formula KE=(1/2)mv**2

DESIGN
1. Prompt from the user mass amount
2.Prompt from the user velocity amount
3.Calculate momentum by using formula Momentum = mass * velocity
4.Calculate the object`s kinetic energy by using formula KE=(1/2) mv**2
5.Display the result

"""
mass = float(input ("Enter the object`s mass: "))
velocity = float (input("Enter the object`s velocity: "))
momentum= mass*velocity
print("The object`s momentum is ", str(momentum))

KE= 1/2 * (mass*velocity**2)

print("The object`s kinetic energy is ", str(KE))