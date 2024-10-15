def f(n):
    b = bin(n)[2:0]
    b = b[::-1]
    x = b.find("1")
    b = b[x:]
    return int(b, 2)


for i in range(1, 100):
    if f(i) == 7:
        print(i)