"""
Program: employeepay.py
Author: Ziynet Akca

This program calculates an employee's total weekly pay.

ANALYSIS:
The user provides 3 inputs: 
1. Hourly wage
2. Total number of regular hours
3. Total number of overtime hours

The program computes:
- Regular pay = wage * regular hours
- Overtime pay = wage * 1.5 * overtime hours
- Total pay = regular pay + overtime pay

DESIGN:
1. Prompt the user for hourly wage
2. Prompt the user for regular hours
3. Prompt the user for overtime hours
4. Calculate regular pay and overtime pay
5. Calculate total pay
6. Display the result
"""
# Step 1: Get inputs from the user
wage = float(input("Enter the hourly wage: $"))
regular_hours = float(input("Enter the regular hours: "))
overtime_hours = float(input("Enter the overtime hours: "))

# Step 2: Calculate regular and overtime pay
regular_pay = wage * regular_hours
overtime_pay = 1.5 * wage * overtime_hours

# Step 3: Calculate total pay
total_pay = regular_pay + overtime_pay

# Step 4: Display the result
print(total_pay)

