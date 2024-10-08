def f(x):
    b = bin(x)[2:]
    if x % 2 == 0:
        b += "00"
    else:
        b += "11"
    return int(b, 2)


for i in range(1, 10000):
    if f(i) > 115:
        print(i)
        break