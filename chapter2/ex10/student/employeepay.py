"""
Program: employeepay.py
Analysis:
This program calculates an employee's total weekly pay.
The weekly pay is the hourly wage multiplied by the total number of regular hours
plus any overtime pay. Overtime pay equals the total overtime hours multiplied
by 1.5 times the hourly wage.

Design (Pseudocode):
1. Prompt the user for hourly wage, regular hours, and overtime hours.
2. Compute the regular pay = wage * regular_hours.
3. Compute the overtime pay = overtime_hours * (1.5 * wage).
4. Compute total pay = regular pay + overtime pay.
5. Display the total weekly pay with a proper label.
"""
#1

wage = float(input("Enter the wage: $"))
regular_hours = float(input("Enter the regular hours: "))
overtime_hours = float(input("Enter the overtime hours: "))


regular_pay = wage * regular_hours
overtime_pay = overtime_hours * (1.5 * wage)
total_pay = regular_pay + overtime_pay


print(f"The total weekly pay is ${round(total_pay, 2)}")
