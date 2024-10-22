def f(n):
    if n % 2 == 0:
        b = n // 2
    else:
        b = n - 1
    if b % 5 == 0:
        b //= 5
    else:
        b -= 1
    if b % 7 == 0:
        b //= 7
    else:
        b -= 1
    return b


k = 0
for i in range(2, 1000):
    if f(i) == 2:
        k += 1
print(k)