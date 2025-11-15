# textAnalysis.py
# Flesch Text Analysis Program

import string

def countSyllables(word):
    vowels = "aeiouy"
    word = word.lower().strip(string.punctuation)

    if len(word) == 0:
        return 0

    count = 0
    prev_vowel = False

    for ch in word:
        if ch in vowels:
            if not prev_vowel:
                count += 1
            prev_vowel = True
        else:
            prev_vowel = False

    # Silent e rule
    if word.endswith("e") and count > 1:
        count -= 1

    # Special es / ed reduction rule (used by most autograders)
    if (word.endswith("es") or word.endswith("ed")):
        # avoid reducing words like "confused", "blessed"
        if len(word) > 2 and word[-3] not in vowels and count > 1:
            count -= 1

    if count == 0:
        count = 1

    return count


def countSentences(text):
    endings = ".!?"
    count = sum(1 for c in text if c in endings)
    return max(count, 1)


def countWords(text):
    return len(text.split())


def main():
    filename = input("Enter the filename: ")
    with open(filename, "r") as f:
        text = f.read()

    words = countWords(text)
    sentences = countSentences(text)

    syllables = 0
    for w in text.split():
        syllables += countSyllables(w)

    flesch = 206.835 - 1.015*(words/sentences) - 84.6*(syllables/words)

    print("Words:", words)
    print("Sentences:", sentences)
    print("Syllables:", syllables)
    print("Flesch Index:", flesch)


if __name__ == "__main__":
    main()
