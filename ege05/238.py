def f(n):
    b = str(n) + str(n % 10)
    b = bin(int(b))[2:]
    if b.count("1") % 2 == 0:
        b += "0"
    else:
        b += "1"
    return int(b, 2)


for i in range(1, 1000):
    if f(i) > 413:
        print(i)