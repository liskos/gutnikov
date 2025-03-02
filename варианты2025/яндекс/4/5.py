def f(n):
    b = bin(n)[2:]
    if n % 2 != 0:
        b = "1" + b[:-2] + "10"
    else:
        b = "10" + b[2:] + "1"
    return int(b, 2)


k = []
for i in range(33,100):
    k.append(f(i))
print(min(k), k)
