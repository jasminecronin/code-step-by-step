def is_all_vowels(s):
    for ch in s:
        if ch.isalpha() and not is_vowel(ch):
            return False
    return True
