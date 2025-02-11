s = 7 ** 270 + 7 ** 170 + 7 ** 70
for x in range(1,10000):
    z = s - x
    k = 0
    while z > 0:
        if z % 7 == 0:
            k += 1
        z //= 7
    if k == 203:
        print(x)
