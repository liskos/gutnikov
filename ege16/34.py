def f(n):
    global r
    r.append(n)
    if n > 0:
        d = n % 10 + f(n // 10)
        r.append(d)
        return d
    else:
        return 0


for i in range(0, 10000):
    r = []
    f(i)
    if len(r) >= 2 and r[1] > 51:
        print(i, f(i))
        break