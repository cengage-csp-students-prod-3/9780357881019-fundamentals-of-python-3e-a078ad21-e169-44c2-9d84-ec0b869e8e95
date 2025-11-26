# recognizer.py
# A simple grammar recognizer for sentences with recursive independent clauses

# Define valid words for simplicity
articles = ["a", "the"]
nouns = ["girl", "boy", "bat", "ball", "cat", "dog"]
verbs = ["hit", "saw", "kicked"]
conjunctions = ["and", "or", "but"]

# Pointer to current word
current = 0

def sentence(words):
    """Recognize a sentence with potentially multiple independent clauses."""
    global current
    if not clause(words):
        return False
    # Handle additional independent clauses recursively
    while current < len(words) and words[current] in conjunctions:
        current += 1  # Skip the conjunction
        if not clause(words):
            return False
    # Acceptable if all words are consumed
    return current == len(words)

def clause(words):
    """Recognize an independent clause: <noun phrase> <verb phrase>."""
    global current
    start = current
    if nounPhrase(words) and verbPhrase(words):
        return True
    current = start  # backtrack if failed
    return False

def nounPhrase(words):
    """Recognize a noun phrase: <article> <noun>."""
    global current
    if current < len(words) and words[current] in articles:
        current += 1
        if current < len(words) and words[current] in nouns:
            current += 1
            return True
    return False

def verbPhrase(words):
    """Recognize a verb phrase: <verb> <noun phrase>."""
    global current
    if current < len(words) and words[current] in verbs:
        current += 1
        if nounPhrase(words):
            return True
    return False

# Main program
if __name__ == "__main__":
    while True:
        sentence_input = input("Enter a sentence or press return to quit: ").strip()
        if not sentence_input:
            break
        words = sentence_input.lower().split()
        current = 0
        if sentence(words):
            print("Ok, grammatically correct")
        else:
            print("Not ok, grammatically incorrect")
