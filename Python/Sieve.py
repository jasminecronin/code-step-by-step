N = int(input("Max value N? "))
s = set()
for i in range(2, N + 1):
    s.add(i)
for num in sorted(s):
    k = num + num
    while k <= N:
        if k in s:
            s.remove(k)
        k += num
print("Primes:", end = " ")
for num in sorted(s):
    print(num, end = " ")



