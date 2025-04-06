def p(n):
    s = ""
    while n > 0:
        s = str(n % 5) + s
        n //= 5
    return s

def f(n):
    s = p(n)
    if n % 2 == 0:
        s = "3" + s + str(n % 5)
    else:
        s = str(n % 4) + s + "4"
    return int(s, 5)


print(f(6), f(13))
for i in range(1, 16):
    print(f(i))