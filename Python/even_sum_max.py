def even_sum():
    n = int(input("how many integers? "))
    sum = 0
    max = 0
    for i in range(n):
        num = int(input("next integer? "))
        if num % 2 == 0:
            sum += num
            if num > max:
                max = num
    print("even sum =", sum)
    print("even max =", max)
