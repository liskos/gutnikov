def d(n, m):
    return n % m == 0


def f(x):
    return (d(x, 23) <= (not d(x,8))) or d(x,A)


k = 0
for A in range(1, 1000):
    if all(f(x) == 1 for x in range(1, 1000)):
        k += 1
print(k)