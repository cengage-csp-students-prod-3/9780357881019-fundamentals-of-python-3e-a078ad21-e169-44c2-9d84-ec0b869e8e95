"""
Program: doctor.py
Author: Ken
Conducts an interactive session of nondirective psychotherapy.
Supports referring back to earlier patient statements.
"""

import random

hedges = ("Please tell me more.",
          "Many of my patients tell me the same thing.",
          "Please continue.")

qualifiers = ("Why do you say that ",
              "You seem to think that ",
              "Can you explain why ")

replacements = {
    "i": "you",
    "me": "you",
    "my": "your",
    "we": "you",
    "us": "you",
    "mine": "yours",
    "you": "I",
    "your": "my",
    "yours": "mine",
    "am": "are",
    "are": "am"
} 

history = []

def reply(sentence):
    """Implements reply strategies including hedges, qualifiers, and earlier statements."""
    history.append(sentence)
    
    
    if len(history) > 3 and random.random() < 0.3:
        past_sentence = random.choice(history[:-1])
        return "Earlier you said that " + changePerson(past_sentence)
    
    if random.randint(1, 4) == 1:
        return random.choice(hedges)
    else:
        return random.choice(qualifiers) + changePerson(sentence)

def changePerson(sentence):
    """Replaces first/second person pronouns correctly, preserves capitalization."""
    words = sentence.split()
    replyWords = []
    for word in words:
        lower_word = word.lower()
        if lower_word in replacements:
            replacement = replacements[lower_word]
            
            if word[0].isupper():
                replacement = replacement.capitalize()
            replyWords.append(replacement)
        else:
            replyWords.append(word)
    return " ".join(replyWords)

def main():
    """Handles interaction between patient and doctor."""
    print("Good morning, I hope you are well today.")
    print("What can I do for you?")
    while True:
        sentence = input("\n>> ")
        if sentence.upper() == "QUIT":
            print("Have a nice day!")
            break
        print(reply(sentence))

if __name__ == "__main__":
    main()
