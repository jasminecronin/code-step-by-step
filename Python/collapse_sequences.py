def collapse_sequences(s, c):
    check = False
    return c_s(s, c, check)
        
def c_s(s, c, b):
    if len(s) == 0:
        return s
    else:
        if s[0] == c and b == False:
            b = True
            string = c_s(s[1:], c, b)
            return s[0] + string
        elif s[0] == c and b == True:
            string = c_s(s[1:], c, b)
            return string
        elif s[0] != c and b == True:
            b = False
            string = c_s(s[1:], c, b)
            return s[0] + string        
        elif s[0] != c and b == False:
            string = c_s(s[1:], c, b)
            return s[0] + string






