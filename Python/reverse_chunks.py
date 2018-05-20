def reverse_chunks(s, k):
    res = ''
    i = 0
    while i + k <= len(s):
        slice = s[i:i+k]
        res += slice[::-1]
        i += k
    j = len(s) % k
    if j != 0:
        res += s[-j:]
    return res
