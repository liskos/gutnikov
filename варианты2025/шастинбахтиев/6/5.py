def ch(n):
    s = ""
    while n > 0:
        s = str(n % 4) + s
        n //= 4
    return s


def f(n):
    c = ch(n)
    if n % 4 == 0:
        c = "2" + c + "03"
    else:
        c += ch(n % 4 * 5)
    return int(c, 4)


k = 0
for i in range(0, 1000,):
    if f(i) <= 567:
        k = i
print(k)