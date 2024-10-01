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


s = []
for i in range(1, 10000):
    if f(i) < 125:
        s.append(f(i))
print(max(s))
