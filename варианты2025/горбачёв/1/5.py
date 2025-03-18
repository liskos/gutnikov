def ch(n):
    s = ""
    while n > 0:
        s = str(n % 4) + s
        n //= 4
    return s

def f(n):
    x = ch(n)
    if sum(map(int, x)) % 2 == 0:
        x = "31" + x + "02"
    else:
        x = "1" + x + str(ch((n % 3) * 7))
    return int(x, 4)

print(f(12), f(11), ch(12), ch(11))