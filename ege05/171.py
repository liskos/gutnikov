def f(n):
    b = bin(n)[2:0].zfill(8)
    a = b[0:2] + b[-7:]
    return int(a, 2)


for i in range(1, 256):
    if f(i) == 10:
        print(i)