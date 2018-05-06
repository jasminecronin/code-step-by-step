def get_days_in_month(n):
    if n == 2:
        return 28
    elif n == 4 or n == 6 or n == 9 or n == 11:
        return 30
    else:
        return 31
