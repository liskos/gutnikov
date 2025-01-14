def f(n):
    b = bin(n)[2:]
    if len(b) % 2 == 0:
        b += "1"
    else:
        b = "1" + b + "0"
    return int(b, 2)


k = 999999
for i in range(0, 1000):
    if f(i) > 666:
        if f(i) < k:
            k = f(i)
print(k)