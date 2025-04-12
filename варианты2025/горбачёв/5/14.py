k = 0
for x in range(1, 1001):
    n = 5 ** x + 31 ** 31 - 46 ** 17 - x
    s = []
    while n > 0:
        s = [n % 7] + s
        n //= 7
    if 1000 > s.count(6) > 100:
        k += 1
print(k)