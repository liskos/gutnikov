def ch(n):
    s = ""
    if n == 0:
        return "0"
    while n > 0:
        s = str(n % 4) + s
        n //= 4
    return s

def f(n):
    x = ch(n)
    if sum(map(int, x)) % 2 == 0:
        x = "31" + x + "02"
    else:
        x = "1" + x + ch((n % 3) * 7)
    return int(x, 4)

for i in reversed(range(1, 10000 )):
    if f(i) < 4528:
        print(i)
        break