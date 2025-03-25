def dev(n):
    s = ""
    while n > 0:
        s = str(n % 9) + s
        n //= 9
    return s

def f(n):
    d = dev(n)
    if sum(map(int, d)) % 2 == 0:
        d += "52"
    else:
        d = "73" + d[2:] + "44"
    return int(d, 9)

for i in range(1, 100000):
    if f(i) > 13950:
        print(i)
        break