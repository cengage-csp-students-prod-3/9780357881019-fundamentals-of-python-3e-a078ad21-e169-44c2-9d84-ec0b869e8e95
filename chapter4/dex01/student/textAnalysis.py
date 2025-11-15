def count_syllables(word):
    word = word.lower()
    vowels = "aeiou"
    syllables = 0
    prev_char_was_vowel = False

    for char in word:
        if char in vowels:
            if not prev_char_was_vowel:  # ardışık ünlü değilse hece say
                syllables += 1
                prev_char_was_vowel = True
        else:
            prev_char_was_vowel = False

    # Kelime sessiz harfle bitiyorsa ve sadece 1 hece sayıldıysa minimum 1 hece
    if syllables == 0:
        syllables = 1

    return syllables
