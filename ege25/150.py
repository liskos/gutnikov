def delit(n):
    s = set()
    for i in range(1, int(n ** 0.5) + 1):
        if i % 2 == 1 and n % i == 0:
            s.add(i)
            s.add(n // i)
    return sorted(s)

for i in range(105000000, 115000000):
    if len(delit(i)) == 5:
        print(delit(i))