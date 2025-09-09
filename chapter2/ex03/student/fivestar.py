"""
Program: fivestar.py
Author: Ziynet Akca
This program calculates the total charge for a customer`s video rentals.
The program should prompt the user for the number of each type of video and output the total cost.

Analysis:
The user provides the number of new videos and the number of old videos.
The program uses the formula==>

newVideoCost= numOfNewVideo * 3.00
oldVideoCost = numOfOldVideo * 2.00
totalCost = newVideoCost + oldVideoCost

Design:
Design:
1. Prompt the user to enter number of new videos and old videos.
2. Calculate cost of new videos: newVideoCost = numOfNewVideo * 3.00
3. Calculate cost of old videos: oldVideoCost = numOfOldVideo * 2.00
4. Compute totalCost = newVideoCost + oldVideoCost
5. Display totalCost


"""
numOfNewVideo = int(input("The number of new videos"))
numOfOldVideo = int (input("The number of old videos"))
newVideoCost= numOfNewVideo * 3.00
oldVideoCost = numOfOldVideo * 2.00
totalCost = newVideoCost + oldVideoCost
print("The total cost is " , str(totalCost))
