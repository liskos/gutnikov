def f(n):
    b = bin(n)[2:]
    b = b + b[-2]
    b = b + b[1]
    return int(b, 2)


print(f(11))
for i in range(2, 1000):
    if f(i) > 100:
        print(i)