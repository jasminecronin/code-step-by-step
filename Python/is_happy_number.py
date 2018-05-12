def sum_of_squares(n):
    sum = 0
    while n != 0:
        sum += (n % 10) ** 2
        n = n // 10
    return sum
    
def is_happy_number(n):
    d = set()
    a = sum_of_squares(n)
    while True:
        if a in d:
            return False
        elif a == 1:
            return True
        else:
            d.add(a)
            a = sum_of_squares(a)
    
