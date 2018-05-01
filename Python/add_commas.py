def add_commas(digits):
    res = ''
    i = len(digits)
    while i >= 4:
        res = ',' + digits[i - 3:i] + res
        i = i - 3
    res = digits[:i] + res
    return res
