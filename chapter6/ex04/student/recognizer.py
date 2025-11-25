# recognizer.py

# --- WORD LISTS ---
articles = {"the", "a", "an"}
nouns = {"boy", "girl", "ball", "bat"}
verbs = {"saw", "hit"}
prepositions = {"with"}
adjectives = {"red", "big", "small"}
conjunctions = {"and"}

# --- PARSER FUNCTIONS ---

def nounPhrase(words, index):
    if index < len(words) and words[index] in articles:
        index += 1
        if index < len(words) and words[index] in adjectives:
            index += 1
        if index < len(words) and words[index] in nouns:
            return True, index + 1
        return False, index
    else:
        if index < len(words) and words[index] in nouns:
            return True, index + 1
        return False, index


def prepPhrase(words, index):
    if index < len(words) and words[index] in prepositions:
        ok, index = nounPhrase(words, index + 1)
        return ok, index
    return False, index


def verbPhrase(words, index):
    if index < len(words) and words[index] in verbs:
        index += 1
        ok, index = nounPhrase(words, index)
        if not ok:
            return False, index
        ok2, newIndex = prepPhrase(words, index)
        if ok2:
            return True, newIndex
        return True, index
    return False, index


def simpleSentence(words, index):
    ok, index = nounPhrase(words, index)
    if not ok:
        return False, index
    return verbPhrase(words, index)


def sentence(words):
    ok, index = simpleSentence(words, 0)
    if not ok:
        return False

    if index < len(words) and words[index] in conjunctions:
        index += 1
        ok2, index = simpleSentence(words, index)
        return ok2 and index == len(words)

    return index == len(words)


# --- MAIN LOOP ---

def main():
    while True:
        user_input = input("Enter a sentence or press return to quit: ").strip()
        if user_input == "":
            break

        words = user_input.lower().split()

        if sentence(words):
            print("correct")
        else:
            print("incorrect")   # REQUIRED FOR THE TESTS


if __name__ == "__main__":
    main()
