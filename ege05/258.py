def f(n):
    b = bin(n)[2:]
    d = b + str(b.count("1") % 2)
    if b.count("1") > b.count("0"):
        d += "0"
    else:
        d += "1"
    return int(d, 2)


k = 0
for i in range(50, 81):
    if f(i) > 80:
        k += 1
print(k)