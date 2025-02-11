def vos(n):
    s = ""
    while n > 0:
        s = str(n % 8) + s
        n //= 8
    return s


def f(n):
    if int(vos(n)) % 2 == 0:
        return int(vos(n).replace("1", "2").replace("3", "2").replace("5", "2").replace("7", "2"), 8)
    return int("3" + vos(n)[1:-1] + "3", 8)


maks = 0
for i in range(1,10000):
    if f(i) < 300:
        if f(i) > maks:
            maks = f(i)
print(maks)