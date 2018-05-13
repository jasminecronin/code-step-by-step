def remove_range(s, min, max):
    for i in range(min, max+1):
        if i in s:
            s.remove(i)
