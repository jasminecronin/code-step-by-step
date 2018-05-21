def word_count(filename):
    s = set()
    file = open(filename, "r")
    for line in file:
        lst = line.split()
        for word in lst:
            s.add(word)
    return len(s)
