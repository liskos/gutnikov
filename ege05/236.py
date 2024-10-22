def f(n):
    b = bin(n)[2:]
    if len(b) % 2 == 0:
        b += "1"
    else:
        b += "0"
    if len(b) % 2 == 0:
        b += "1"
    else:
        b += "0"
    return int(b, 2)


for i in range(1, 1000):
    if f(i) < 171:
        print(i)