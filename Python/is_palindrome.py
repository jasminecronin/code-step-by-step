def is_palindrome(s):
    str = s.lower()
    for i in range(len(str) // 2):
        if str[i] != str[-(i + 1)]:
            return False
    return True
