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
    if n % 25 != 0:
        b = pyat(n) + str(n % 25)
    return int(b, 5)


print(f(100))