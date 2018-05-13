def average_value_in_file(filename):
    count = 0
    sum = 0
    file = open(filename, "r")
    for num in file:
        sum += float(num)
        count += 1
    if count == 0:
        return 0.0
    else:
        return sum / count
