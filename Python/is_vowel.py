def is_vowel(s):
    vowels = 'AEIOUaeiou'
    if len(s) != 1:
        return False
    if s in vowels:
        return True
    return False
