def delit(n):
    s = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            s.add(i)
            s.add(n // i)
    return sorted(s)

for i in range(2532000, 2532160 + 1):
    if len(delit(i)) == 2:
        print(delit(i))