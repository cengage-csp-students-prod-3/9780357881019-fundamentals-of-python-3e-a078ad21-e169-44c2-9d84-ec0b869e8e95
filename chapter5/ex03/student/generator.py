"""
Program: generator.py
Author: Ken
Generates and displays sentences using a simple grammar
and vocabulary. Words are chosen at random.
"""

import random

def getWords(filename):
    """Read words from a file and return them as a tuple."""
    temp_list = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                temp_list.extend(line.split())
    except FileNotFoundError:
        print(f"File {filename} not found.")
    return tuple(temp_list)

# Initialize vocabulary from text files
articles = getWords("articles.txt")
nouns = getWords("nouns.txt")
verbs = getWords("verbs.txt")
prepositions = getWords("prepositions.txt")

def sentence():
    """Builds and returns a sentence."""
    return nounPhrase() + " " + verbPhrase()

def nounPhrase():
    """Builds and returns a noun phrase."""
    return random.choice(articles) + " " + random.choice(nouns)

def verbPhrase():
    """Builds and returns a verb phrase."""
    return random.choice(verbs) + " " + nounPhrase() + " " + \
           prepositionalPhrase()

def prepositionalPhrase():
    """Builds and returns a prepositional phrase."""
    return random.choice(prepositions) + " " + nounPhrase()

def main():
    """Allows the user to input the number of sentences to generate."""
    number = int(input("Enter the number of sentences: "))
    for count in range(number):
        print(sentence())

# The entry point for program execution
if __name__ == "__main__":
    main()
