def f(n):
    b = bin(n)[2:]
    b = b + str((b.count("1") % 2))
    b = b + str((b.count("1") % 2))
    return int(b, 2)


print(f(13))
k = 0
for i in range(1, 1000):
    if 210 <= f(i) <= 260:
        k += 1
print(k)