def tr(x):
    s = ""
    while x > 0:
        s += str(x % 3)
        x //= 3
    return s[::-1]

def f(x):
    t = tr(x)
    if x % 2 == 0:
        t = "1" + t + '00'
    else:
        t += tr(sum(map(int, t)))
    return int(t, 3)


print(f(4), f(7))
for i in range(1, 1000):
    if f(i) > 168:
        print(i)
        break