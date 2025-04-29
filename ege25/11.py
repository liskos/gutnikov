def delit(n):
    a = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            a.add(i)
            a.add(n // i)
    return sorted(a)


for i in range(164700, 164752 + 1):
    if len(delit(i)) == 6:
        print(i, *delit(i))