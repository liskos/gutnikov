def p(n):
    s = ""
    while n > 0:
        s = str(n % 5) + s
        n //= 5
    return s


for x in range(1, 2043):
    s = 25 ** 61 + 5 ** 178 - x
    if p(s).count("0") == 60:
        print(x)