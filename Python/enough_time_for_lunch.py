def enough_time_for_lunch(h1, m1, h2, m2):
    if (h2 - h1) < 0:
        return False
    elif (h2 - h1) > 1:
        return True
    elif (h2 - h1) == 1:
        if (m2 + 60 - m1) < 45:
            return False
        else:
            return True
    else:
        if (m2 - m1) < 45:
            return False
        else: return True
