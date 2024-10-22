def f(n):
    b = bin(n)[2:]
    if n % 2 != 0:
        a = b[:-2] + "10"
    else:
        a = "10" + b[2:] + "1"
    return int(a, 2)


print(f(5))
for i in range(27, 1000):
    print(f(i))