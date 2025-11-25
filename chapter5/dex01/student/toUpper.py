"""
Program: toUpper.py
Author: Jack
Converts all words in a list to uppercase.
"""


listOfWords = ["Apple", "orange", "banana"]


for i in range(len(listOfWords)):
    listOfWords[i] = listOfWords[i].upper()


print(listOfWords)
