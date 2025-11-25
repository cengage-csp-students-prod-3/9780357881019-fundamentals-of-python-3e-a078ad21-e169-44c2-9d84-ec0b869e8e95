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

def changePerson(sentence):
    """Replaces first person pronouns with second person pronouns, and vice versa."""
    words = sentence.split()
    replyWords = []
    for word in words:
        # Küçük harfe çevirip sözlükten kontrol et
        lower_word = word.lower()
        if lower_word in replacements:
            # Orijinal kelimenin büyük/küçük harfini korumak için:
            replacement = replacements[lower_word]
            if word[0].isupper():
                replacement = replacement.capitalize()
            replyWords.append(replacement)
        else:
            replyWords.append(word)
    return " ".join(replyWords)
