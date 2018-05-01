def month_apart(m1, d1, m2, d2):
    if m1 == m2:
        return False
    elif abs(m1 - m2) > 1:
        return True
    else:
        if m1 < m2:
            return d2 >= d1
        else:
            return d1 >= d2
