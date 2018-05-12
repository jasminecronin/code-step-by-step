def num_unique_values(lst):
    s = set()
    for item in lst:
        if item not in s:
            s.add(item)
    return len(s)
    
