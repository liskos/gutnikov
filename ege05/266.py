def f(n):
    if n % 3 == 0:
        b = n // 3
    else:
        b = n - 1
    if b % 5 == 0:
        b //= 5
    else:
        b -= 1
    if b % 11 == 0:
        b //= 11
    else:
        b -= 1
    return b


k = 0
for i in range(2, 2000):
    if f(i) == 8:
        k += 1
print(k)