"""
Program: toUpper.py
Author: Jack
Converts all words in a list to uppercase.
"""

# Orijinal liste
listOfWords = ["Apple", "orange", "banana"]

# Her kelimeyi büyük harfe çevir
for i in range(len(listOfWords)):
    listOfWords[i] = listOfWords[i].upper()

# Sonucu yazdır
print(listOfWords)
