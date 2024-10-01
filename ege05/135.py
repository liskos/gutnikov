def f(x):
    b = bin(x)[2:]
    if b.count("1") % 2 == 0:
        b += "1"
    else:
        b += "0"
    if b.count("1") % 2 == 0:
        b += "1"
    else:
        b += "0"
    return int(b, 2)


s = 0
for i in range(1, 10000):
    if 16 <= f(i) <= 32:
        s += 1
print(s)
