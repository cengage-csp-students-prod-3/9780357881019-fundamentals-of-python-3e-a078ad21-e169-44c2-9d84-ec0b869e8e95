# textAnalysis.py
# Flesch Text Analysis Program

import string

def countSyllables(word):
    """Counts syllables in a word, treating consecutive vowels as ONE syllable."""
    vowels = "aeiouy"
    word = word.lower().strip(string.punctuation)

    if len(word) == 0:
        return 0

    count = 0
    previousWasVowel = False

    for char in word:
        if char in vowels:
            if not previousWasVowel:
                count += 1
            previousWasVowel = True
        else:
            previousWasVowel = False

    # remove silent e rule
    if word.endswith("e") and count > 1:
        count -= 1

    # every word has at least 1 syllable
    if count == 0:
        count = 1

    return count


def countSentences(text):
    """Counts sentences based on punctuation."""
    sentenceEndings = ".!?"
    count = 0
    for char in text:
        if char in sentenceEndings:
            count += 1
    return max(1, count)


def countWords(text):
    """Counts words by splitting on whitespace."""
    words = text.split()
    return len(words)


def main():
    filename = input("Enter the filename: ")
    
    with open(filename, "r") as file:
        text = file.read()

    words = countWords(text)
    sentences = countSentences(text)

    syllables = 0
    for w in text.split():
        syllables += countSyllables(w)

    fleschIndex = 206.835 - 1.015 * (words / sentences) - 84.6 * (syllables / words)

    print("Words:", words)
    print("Sentences:", sentences)
    print("Syllables:", syllables)
    print("Flesch Index:", fleschIndex)


if __name__ == "__main__":
    main()
