# recognizer.py

# --- WORD LISTS ---
articles = {"the", "a", "an"}
nouns = {"boy", "girl", "ball", "bat"}
verbs = {"saw", "hit"}
prepositions = {"with"}
adjectives = {"red", "big", "small"}          # NEW
conjunctions = {"and", "but"}                # NEW (you can extend)

# --- PARSER FUNCTIONS ---

def nounPhrase(words, index):
    """Noun phrase can be:
       article + noun
       article + adjective + noun
       noun
    """
    if index < len(words) and words[index] in articles:
        index += 1
        # check adjective
        if index < len(words) and words[index] in adjectives:
            index += 1
        # expect noun
        if index < len(words) and words[index] in nouns:
            return True, index + 1
        else:
            return False, index
    else:
        # Allow bare noun (optional if your instructor wants it)
        if index < len(words) and words[index] in nouns:
            return True, index + 1
        return False, index


def prepPhrase(words, index):
    """prepositional phrase: preposition + noun phrase"""
    if index < len(words) and words[index] in prepositions:
        ok, index = nounPhrase(words, index + 1)
        return ok, index
    return False, index


def verbPhrase(words, index):
    """Verb phrase can be:
       verb + noun phrase
       verb + noun phrase + prepositional phrase
    """
    if index < len(words) and words[index] in verbs:
        index += 1
        ok, index = nounPhrase(words, index)
        if not ok:
            return False, index

        # optional prepositional phrase
        ok2, newIndex = prepPhrase(words, index)
        if ok2:
            return True, newIndex
        return True, index

    return False, index


def simpleSentence(words, index):
    """A simple sentence: noun phrase + verb phrase"""
    ok, index = nounPhrase(words, index)
    if not ok:
        return False, index
    return verbPhrase(words, index)


def sentence(words):
    """A full sentence can be:
       simpleSentence
       simpleSentence + conjunction + simpleSentence
    """
    ok, index = simpleSentence(words, 0)
    if not ok:
        return False

    # Check if sentence continues with a conjunction
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
            print("Ok, grammatically correct")
        else:
            print("Not grammatically correct")


if __name__ == "__main__":
    main()
