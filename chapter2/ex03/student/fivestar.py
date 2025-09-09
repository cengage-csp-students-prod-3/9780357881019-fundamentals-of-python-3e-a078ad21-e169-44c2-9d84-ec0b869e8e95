"""
Program: fivestar.py
Author: Ziynet Akca

This program calculates the total charge for a customer’s video rentals.
It prompts the user for the number of new videos and oldies rented and
computes the total cost based on fixed rates.

Analysis:
- User inputs:
    - Number of new videos
    - Number of oldies
- Prices:
    - New videos: $3.00 per night
    - Oldies: $2.00 per night
- Output: Total cost of the rentals

Design (pseudocode):
1. Prompt the user to enter the number of new videos
2. Prompt the user to enter the number of oldies
3. Compute newVideoCost = number of new videos * 3.00
4. Compute oldVideoCost = number of oldies * 2.00
5. Compute totalCost = newVideoCost + oldVideoCost
6. Display totalCost formatted exactly as "The total cost is $<amount>"
"""

# Request the number of videos
numOfNewVideo = int(input("Enter the number of new videos: "))
numOfOldVideo = int(input("Enter the number of oldies: "))

# Compute costs
newVideoCost = numOfNewVideo * 3.00
oldVideoCost = numOfOldVideo * 2.00
totalCost = newVideoCost + oldVideoCost

# Display total cost in the exact format expected
print("Enter the number of new videos: " + str(numOfNewVideo))
print("Enter the number of oldies: " + str(numOfOldVideo))
print("The total cost is $" + str(totalCost))