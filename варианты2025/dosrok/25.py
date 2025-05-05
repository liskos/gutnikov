def delit(n):
    s = set()
    for i in range(2, int(n ** 0.5) + 1):
        if i != 7 and n % i == 0 and i % 10 == 7:
            s.add(i)
            s.add(n // i)
    return sorted(s)

for i in range(1125000, 1125040):
    if len(delit(i)) > 0:
        print(i, delit(i)[0])

print(delit(1125011))