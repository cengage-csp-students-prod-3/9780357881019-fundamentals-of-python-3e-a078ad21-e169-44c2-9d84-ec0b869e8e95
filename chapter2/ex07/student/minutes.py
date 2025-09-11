"""
Program: minutes.py
Author: Ziynet Akca

This program calculates the number of minutes in a given number of years.

ANALYSIS
The user provides the number of years as input.
The program calculates how many minutes there are in that period.
1 year = 365 days
1 day = 24 hours
1 hour = 60 minutes

DESIGN
1. Prompt the user for the number of years.
2. Convert years into days (years * 365).
3. Convert days into hours (days * 24).
4. Convert hours into minutes (hours * 60).
5. Display the total number of minutes.
"""

years = int(input("Enter the number of years: "))
minutes = years * 365 * 24 * 60
print("The number of minutes in", years, "year(s) is", minutes)

