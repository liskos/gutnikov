def f(n):
    b = bin(n)[2:].zfill(8)
    a = b[:2] + b[-2:]
    return int(a, 2)


for i in range(131, 256):
    if f(i) == 10:
        print(i)