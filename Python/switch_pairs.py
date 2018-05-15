def switch_pairs(s):
    res = ''
    i = 0
    if len(s) < 2:
        return s
    while i < len(s) - 1:
        res += s[i + 1]
        res += s[i]
        i += 2
    if len(s) % 2 != 0:
        res += s[-1]
    return res
