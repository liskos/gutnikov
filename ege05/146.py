def f(n):
    b = bin(n)[2:]
    b1 = b + b[-1]
    if b.count("1") % 2 == 0:
        b1 += "0"
    else:
        b1 += "1"
    if b1.count("1") % 2 == 0:
        b1 += "0"
    else:
        b1 += "1"
    return int(b1, 2)



s = []
for i in range(1, 1000):
    if f(i) > 130:
        s.append(f(i))
print(min(s))