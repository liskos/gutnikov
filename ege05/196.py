def f(n):
    b = bin(n)[2:]
    b = b + str((b.count("1") % 2))
    b = b + str((b.count("1") % 2))
    return int(b, 2)


print(f(13))
for i in range(1, 1000):
    if f(i) < 70:
        print(f(i))