def union_sets(sets):
    r = set()
    for s in sets:
        for element in s:
            r.add(element)
    return r
