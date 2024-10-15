def f(n):
    b = bin(n)[2:].zfill(8)
    a = b[:2] + b[-2:]
    return int(a, 2)


for i in range(0, 110):
    if f(i) == 7:
        print(i)