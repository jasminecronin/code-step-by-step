sum = 0
count = 0
while True:
    num = int(input("Integer? "))
    if num == 0:
        break
    if (num % 2 == 0):
        sum += num
        count += 1
print("Average:", sum / count)
