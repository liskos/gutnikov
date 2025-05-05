def delit(n):
    s = set()
    for i in range(1, int(n ** 0.5) + 1):
        if i % 2 == 1 and n % i == 0:
            s.add(i)
            s.add(n // i)
    return sorted(s)

for i in range(2095133039, 2095133043):
    if len(delit(i)) == 1600:
        print(i)
        break