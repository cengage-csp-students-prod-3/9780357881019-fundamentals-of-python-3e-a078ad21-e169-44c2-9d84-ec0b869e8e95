"""
Program: lightyear.py
Author: Ziynet Akca

This program calculates the distance that light travels in a given number of years.

ANALYSIS
The user provides the number of years as input.
The program calculates the distance by multiplying:
- The speed of light (3 * 10^8 meters/second)
- The number of seconds in a year
- The number of years

1 minute = 60 seconds
1 hour = 60 minutes
1 day = 24 hours
1 year = 365 days

DESIGN
1. Prompt the user for the number of years.
2. Calculate the number of seconds in one year.
3. Multiply seconds in a year by the speed of light.
4. Multiply by the number of years given by the user.
5. Display the total distance traveled by light.
"""

years = int(input("Enter the number of years: "))

# Step 2: constants
speed_of_light = 3 * 10**8   # meters per second
seconds_in_year = 365 * 24 * 60 * 60

# Step 3: calculation
distance = years * speed_of_light * seconds_in_year

# Step 4: output
print("Light travels", distance, "meters in", years, "years.")

