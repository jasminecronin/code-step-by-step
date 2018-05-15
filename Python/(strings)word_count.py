def word_count(s):
    if len(s) == 0:
        return 0
    count = 0
    word = False
    for letter in s:
        if letter != ' ':
            word = True
        elif letter == ' ' and word == True:
            count += 1
            word = False
    if s[-1] != ' ':
        count += 1
    return count
