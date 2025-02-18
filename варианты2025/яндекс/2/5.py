def pyat(n):
    s = ""
    while n > 0:
        s = str(n % 5) + s
        n //= 5
    return s


def f(n):
    b = ""
    if n % 25 == 0:
        b = pyat(n)[-3:] + pyat(n)
    elif n % 25 != 0:
        b = pyat(n) + pyat(n % 25)
    return int(b, 5)


print(f(25), f(26))
for i in range(1, 10000):
    if f(i) > 10000:
        print(i)
        break