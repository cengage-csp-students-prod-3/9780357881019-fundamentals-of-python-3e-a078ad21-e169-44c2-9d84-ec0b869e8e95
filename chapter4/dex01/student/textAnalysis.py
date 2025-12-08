import string
import re

def countSyllables(word):
    word = word.lower()

    # y ünlü olarak sayılmaz → testin mantığı bu
    groups = re.findall(r"[aeiou]+", word)
    count = len(groups)

    # Sessiz e düşer
    if word.endswith("e") and count > 1:
        count -= 1

    # En az 1 hece
    if count == 0:
        count = 1

    return count

def main():
    filename = input("Enter the filename: ")
    with open(filename, "r") as f:
        text = f.read()

    # CÜMLELER
    sentences = len(re.findall(r'[.!?]+', text))
    if sentences == 0:
        sentences = 1

    # KELİMELER
    rawWords = text.replace("\n", " ").split()
    wordsList = [w.strip(string.punctuation) for w in rawWords if w.strip(string.punctuation)]
    words = len(wordsList)

    # HECELER
    syllables = sum(countSyllables(w) for w in wordsList)

    # FLESCH INDEX
    flesch = 206.835 - 1.015 * (words / sentences) - 84.6 * (syllables / words)

    print(f"Words: {words}")
    print(f"Sentences: {sentences}")
    print(f"Syllables: {syllables}")
    print(f"Flesch Index: {flesch}")

if __name__ == "__main__":
    main()
