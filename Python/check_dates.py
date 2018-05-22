def check_dates(filename):
    file = open(filename, 'r')
    for line in file:
        m1, d1, m2, d2 = [int(i) for i in line.split()]
        differ = False
        if abs(m1 - m2) > 1:
            differ = True
        elif abs(m1 - m2) == 1:
            if (m1 < m2) and (d2 - d1) >= 0:
                differ = True
            elif (m1 > m2) and (d1 - d2) >= 0:
                differ = True
        if differ:
            print("{}/{} and {}/{} differ by one full month or more!".format(m1, d1, m2, d2))
        else:
            print("{}/{} and {}/{} are within one month of each other.".format(m1, d1, m2, d2))
