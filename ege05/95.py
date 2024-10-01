def f(n):
    b = bin(n)[2:]
    if b.count("1") % 2 == 0:
        b += "0"
    else:
        b += "1"
    if b.count("1") % 2 == 0:
        b += "0"
    else:
        b += "1"
    return int(b, 2)


v = []
for i in range(1, 10000):
    if f(i) > 130:
        v.append(f(i))
print(min(v))