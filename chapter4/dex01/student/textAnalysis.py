import string
import re

def countSyllables(word):
    word = word.lower()

    # Find vowel groups (handles consecutive vowels correctly)
    groups = re.findall(r"[aeiouy]+", word)
    count = len(groups)

    # Silent 'e' rule
    if word.endswith("e") and count > 1:
        count -= 1

    # At least 1 syllable
    if count == 0:
        count = 1

    return count

def main():
    filename = input("Enter the filename: ")
    with open(filename, "r") as f:
        text = f.read()

    # SENTENCES
    sentences = len(re.findall(r'[.!?]+', text))
    if sentences == 0:
        sentences = 1

    # WORDS
    rawWords = text.replace("\n", " ").split()
    wordsList = []

    for w in rawWords:
        w = w.strip(string.punctuation)
        if w:
            wordsList.append(w)

    words = len(wordsList)

    # SYLLABLES
    syllables = sum(countSyllables(w) for w in wordsList)

    # FLESCH INDEX
    flesch = 206.835 - 1.015 * (words / sentences) - 84.6 * (syllables / words)

    print(f"Words: {words}")
    print(f"Sentences: {sentences}")
    print(f"Syllables: {syllables}")
    print(f"Flesch Index: {flesch}")

if __name__ == "__main__":
    main()
