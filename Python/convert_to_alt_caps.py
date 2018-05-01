def convert_to_alt_caps(str):
    res = ''
    caps = False
    for ch in str:
        if ch == ' ':
            res += ch
        elif (caps):
            res += ch.upper()
            caps = False
        else:
            res += ch.lower()
            caps = True
    return res
