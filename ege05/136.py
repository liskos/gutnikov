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


a = set()
for i in range(1, 10000):
    if 16 <= f(i) <= 32:
        a.add(f(i))
print(17-len(a))
