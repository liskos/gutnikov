def ch(n):
    s = ""
    while n > 0:
        s = str(n % 4) + s
        n = n // 4
    return  s


def f(n):
    c = ch(n)
    if len(c) % 2 == 0:
        c = c[:len(c) // 2] + "0" + c[len(c) // 2:]
    return int(c)


k = 0
print(f(6))
for i in range(1, 1000):
    if f(i) <= 180:
        k = i
        print(i)
print(k)

