def f(x):
    b = bin(x)[2:]
    if b.count("1") % 2 == 0:
        b += "0"
    else:
        b += "1"
    if b.count("1") % 2 == 0:
        b += "0"
    else:
        b += "1"
    return int(b, 2)


s = 0
k = 0
for i in range(1, 10000):
    k += 1
    if 16 <= f(i) <= 32:
        s += 1
print(k - s)