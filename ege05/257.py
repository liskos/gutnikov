def f(n):
    b = bin(n)[2:]
    d = b + str(b.count("1") % 2)
    if b.count("1") > b.count("0"):
        d += "0"
    else:
        d += "1"
    return int(d, 2)


for i in range(1, 1000):
    if f(i) > 80:
        print(f(i))