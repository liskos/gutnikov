def f(n):
    b = bin(n)[2:]
    b = b[::-1]
    return int(b, 2)


for i in range(1, 101):
    if f(i) == 9:
        print(i)