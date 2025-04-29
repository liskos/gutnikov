def p(n):
    a = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            a.add(i)
            a.add(n // i)
        if len(a) >= 10:
            break
    if len(a) < 5:
        return 0, 0
    a = sorted(a)
    return a[0] * a[1] * a[2] * a[3] * a[4], a[4]

k = 0
for n in range(300_000_001, 10**10):
    f, d = p(n)
    if f % 100 == 31 and f <= n:
        print(f, d)
        k += 1
        if k == 5:
            break