"""
Program: taxform.py
Author: Your Name

This program computes a person's income tax.

Analysis:
- The user provides their gross income and the number of dependents.
- The program uses fixed constants: tax rate, standard deduction, and deduction per dependent.
- The program computes the taxable income, then applies the tax rate to find the income tax.

Design (pseudocode):
1. Set constants: TAX_RATE, STANDARD_DEDUCTION, DEPENDENT_DEDUCTION
2. Input grossIncome from the user
3. Input numDependents from the user
4. Compute taxableIncome = grossIncome - STANDARD_DEDUCTION - (DEPENDENT_DEDUCTION * numDependents)
5. Compute incomeTax = taxableIncome * TAX_RATE
6. Output incomeTax rounded to 2 decimal places
"""

# Initialize the constants
TAX_RATE = 0.20
STANDARD_DEDUCTION = 10000.0
DEPENDENT_DEDUCTION = 3000.0

# Request the inputs
grossIncome = float(input("Enter the gross income: "))
numDependents = int(input("Enter the number of dependents: "))

# Compute the income tax
taxableIncome = grossIncome - STANDARD_DEDUCTION - (DEPENDENT_DEDUCTION * numDependents)
incomeTax = taxableIncome * TAX_RATE

# Display the income tax (rounded to 2 decimal places, nicely formatted)
print("The income tax is ${:.2f}".format(incomeTax))
