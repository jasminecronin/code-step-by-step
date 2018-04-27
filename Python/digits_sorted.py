def digits_sorted(n):
    if n < 0:
        n = abs(n)
    return d_sorted(n)

def d_sorted(n):
    if n < 10:
        return True
    else:
        last_digit = n % 10
        n = n // 10
        second_last_digit = n % 10
        if  last_digit >= second_last_digit:
            return d_sorted(n)
        else:
            return False
        









