def f(x):
    b = bin(x)[2:]
    b += b[-1]
    if b.count("1") % 2 == 0:
        b += "0"
    else:
        b += "1"
    if b.count("1") % 2 == 0:
        b += "0"
    else:
        b += "1"
    return int(b, 2)



for i in range(1, 1000):
    if f(i) > 114:
        print(i)
        break