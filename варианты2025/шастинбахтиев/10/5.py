def tr(n):
    s = ""
    while n > 0:
        s = str(n % 3) + s
        n //= 3
    return s


def f(n):
    s = tr(n)
    if n % 3 == 0:
        s = s[-2:] + s
    else:
        s = tr(sum(map(int, s))) + s
    return int(s, 3)


s = set()
for i in range(1, 1000):
    if f(i) % 2 == 1 and f(i) > 418:
        s.add(f(i))
print(min(s))