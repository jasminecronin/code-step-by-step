def three_consecutive(a, b, c):
    l = [a, b, c]
    l.sort()
    if l[1] == l[0] + 1 and l[2] == l[1] + 1:
        return True
    return False
