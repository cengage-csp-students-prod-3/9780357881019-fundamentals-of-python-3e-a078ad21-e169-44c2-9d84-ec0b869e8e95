"""
Program: generator.py
Author: Ken
Generates and displays sentences using a simple grammar
and vocabulary. Words are chosen at random.
"""

import random

# Vocabulary
articles = ("A", "THE")
nouns = ("BOY", "GIRL", "BAT", "BALL")
verbs = ("HIT", "SAW", "LIKED")
prepositions = ("WITH", "BY")
adjectives = ("RED", "LITTLE", "HAPPY", "SORE")
conjunctions = ("AND", "BUT", "OR")

def sentence():
    """Builds and returns a sentence, optionally with a second clause."""
    first_clause = nounPhrase() + " " + verbPhrase()
    
    # Optional second independent clause with a conjunction (50% chance)
    if random.random() < 0.5:
        conj = random.choice(conjunctions)
        second_clause = nounPhrase() + " " + verbPhrase()
        return first_clause + " " + conj + " " + second_clause
    else:
        return first_clause

def nounPhrase():
    """Builds and returns a noun phrase with optional adjective."""
    phrase = random.choice(articles) + " "
    # Optional adjective (50% chance)
    if random.random() < 0.5:
        phrase += random.choice(adjectives) + " "
    phrase += random.choice(nouns)
    return phrase

def verbPhrase():
    """Builds and returns a verb phrase with optional prepositional phrase."""
    phrase = random.choice(verbs) + " " + nounPhrase()
    # Optional prepositional phrase (50% chance)
    if random.random() < 0.5:
        phrase += " " + prepositionalPhrase()
    return phrase

def prepositionalPhrase():
    """Builds and returns a prepositional phrase."""
    return random.choice(prepositions) + " " + nounPhrase()

def main():
    """Allows the user to input the number of sentences to generate."""
    number = int(input("Enter the number of sentences: "))
    for _ in range(number):
        print(sentence())

# Entry point for program execution
if __name__ == "__main__":
    main()
