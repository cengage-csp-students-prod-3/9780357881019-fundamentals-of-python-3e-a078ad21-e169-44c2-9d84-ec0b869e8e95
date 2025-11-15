def count_syllables(word):
    word = word.lower()
    vowels = "aeiou"
    syllables = 0
    prev_vowel = False

    for char in word:
        if char in vowels:
            if not prev_vowel:
                syllables += 1
            prev_vowel = True
        else:
            prev_vowel = False

    if syllables == 0:
        syllables = 1

    return syllables


def main():
    filename = input("Enter the file name: ")
    file = open(filename, "r")

    text = file.read()
    file.close()

    # Sentences count
    sentences = 0
    for ch in text:
        if ch in ".!?":
            sentences += 1

    # Words list
    words = text.split()
    word_count = len(words)

    # Syllables count
    syllables = 0
    for word in words:
        syllables += count_syllables(word)

    # Metrics
    words_per_sentence = word_count / sentences
    syllables_per_word = syllables / word_count

    # Flesch Index formula
    flesch_index = 206.835 - (1.015 * words_per_sentence) - (84.6 * syllables_per_word)

    # EXACT output format required by the autograder
    print("The Flesch Index is", flesch_index)
    print("The Average Number of Words Per Sentence is", words_per_sentence)
    print("The Average Number of Syllables Per Word is", syllables_per_word)


if __name__ == "__main__":
    main()
