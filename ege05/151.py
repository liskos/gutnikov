def f(n):
    b = bin(n)[2:]
    if n % 2 == 0:
        b += "01"
    else:
        b += "10"
    return int(b, 2)


for i in range(1, 10000):
    if f(i) > 62:
        print(f(i))
