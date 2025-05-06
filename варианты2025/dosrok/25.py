def delit(n):
    s = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            s.add(i)
            s.add(n // i)
    return sorted([x for x in s if x % 10 == 7 and x != 7])


k = 0
for i in range(1125001, 1125040):
    if len(delit(i)) > 0:
        print(i, delit(i)[0])
        k += 1
        if k == 5:
            break

