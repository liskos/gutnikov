def f(n):
    b = bin(n)[2:]
    b = b + str((int(b.count("1")) % 2))
    b = b + str((int(b.count("1")) % 2))
    return int(b,2)


for i in range(1, 1000):
    if f(i) > 198:
        print(f(i))
        break
