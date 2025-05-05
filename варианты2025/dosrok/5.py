def f(n):
    b = bin(n)[2:]
    if b.count("1") % 2 == 0:
        b = "10" + b[2:] + "0"
    else:
        b = "11" + b[2:] + "1"
    return int(b, 2)

s = []
for n in range(1, 1000):
    if f(n) > 480:
        s.append(n)
print(min(s))