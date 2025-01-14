def f(n):
    b = bin(n)[2:]
    if b.count("1") % 2 == 0:
        b += "0"
        b = "10" + b[2:]
    else:
        b += "1"
        b = "11" + b[2:]
    return int(b, 2)

for i in range(0, 1000):
    if f(i) > 171:
        print(i)
