def max_length(s):
    if len(s) == 0:
        return 0
    length = set()
    for item in s:
        length.add(len(item))
    return max(length)
