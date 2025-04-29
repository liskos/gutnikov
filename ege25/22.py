def delit(n):
    a = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
                a.add(i)
                a.add(n // i)
    return sorted([x for x in a if x % 2 == 0], reverse=True)


for i in range(190201, 190280 + 1):
    if len(delit(i)) == 4:
        print(i, *delit(i))
