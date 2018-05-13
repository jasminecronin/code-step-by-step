def twice(v):
    s = set()
    for item in v:
        if v.count(item) == 2:
            s.add(item)
    return s
    
