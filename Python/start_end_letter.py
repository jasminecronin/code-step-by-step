def start_end_letter(c):
    print("Looking for two \"{}\" words in a row.".format(c))
    count = 0
    while True:
        inp = input("Type a word: ")
        word = inp.lower()
        if word[0] == c and word[-1] == c:
            count += 1
        else:
            count = 0
        if count == 2:
            break
    print("\"{}\" is for \"{}\"".format(c, inp))
        
