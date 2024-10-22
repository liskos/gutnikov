def f(n):
    if n % 3 == 0:
        b = n // 3
    else:
        b = n - 1
    if b % 7 == 0:
        b //= 7
    else:
        b -= 1
    if b % 11 == 0:
        b //= 11
    else:
        b -= 1
    return b


k = 0
for i in range(2, 1500):
    if f(i) == 6:
        k += 1
print(k)