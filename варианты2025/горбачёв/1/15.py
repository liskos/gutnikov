def d(n, m):
    return n % m == 0

def f(x):
    return (55 <= x <= 75) <= (d(x, a) or (not d(x, 35)))

for a in range(1, 1000):
    if all(f(x) for x in range(1, 1000)):
        print(a)