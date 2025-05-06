def prime_number(n):
    a = [True] * n
    a[0] = a[1] = False
    for i in range(2, n):
        if a[i]:
            for j in range(i * i, n, i):
                a[j] = False
    return [i for i in range(n) if a[i]]

def delit(n):
    s = set()
    for z in range(1, int(n ** 0.5) + 1):
        if n % z == 0:
                s.add(z)
                s.add(n // z)
    return sorted([x for x in s if x % 2 == 1])


a = []
p = prime_number(104)
p = [x ** 4 for x in p if x % 2 == 1]
for x in p:
    while x < 105_000_000:
        x *= 2
    if x < 115_000_000:
        a.append(x)
a.sort()
for i in a:
    if len(delit(i))==5:
        print(i, delit(i)[-1])