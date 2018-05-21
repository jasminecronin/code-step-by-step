def remove_duplicates(s):
    if len(s) == 0:
        return s
    res = s[0]
    for i in range(1, len(s)):
        if s[i] != s[i - 1]:
            res += s[i]
    return res
