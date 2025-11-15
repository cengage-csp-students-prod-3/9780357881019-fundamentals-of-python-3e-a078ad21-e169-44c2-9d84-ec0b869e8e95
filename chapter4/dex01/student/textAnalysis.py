def countSyllables(word):
    word = word.lower()
    vowels = "aeiouy"
    count = 0
    prevVowel = False

    for i, ch in enumerate(word):
        if ch in vowels:
            if not prevVowel:
                count += 1
            prevVowel = True
        else:
            prevVowel = False

    if word.endswith("e") and count > 1:
        count -= 1

    if count == 0:
        count = 1

    return count

def main():
    filename = input("Enter the filename: ")
    with open(filename, "r") as f:
        text = f.read()

    # Sentences
    sentences = 0
    for ch in text:
        if ch in ".!?":
            sentences += 1
    if sentences == 0:
        sentences = 1

    # Words
    wordsList = text.replace("\n", " ").split()
    words = len(wordsList)

    # Syllables
    syllables = sum(countSyllables(word) for word in wordsList)

    # Flesch Index
    flesch = 206.835 - 1.015 * (words / sentences) - 84.6 * (syllables / words)

    print(f"Words: {words}")
    print(f"Sentences: {sentences}")
    print(f"Syllables: {syllables}")
    print(f"Flesch Index: {flesch}")

if __name__ == "__main__":
    main()
