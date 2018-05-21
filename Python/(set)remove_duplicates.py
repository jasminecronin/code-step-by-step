def remove_duplicates(v):
    s = set()
    i = 0
    while i < len(v):
        if v[i] in s:
            del v[i]
        else:
            s.add(v[i])
            i += 1
