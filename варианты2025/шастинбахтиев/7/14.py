c = []
for x in range(0,15):
    m = int("43203", 15) + x * 15
    n = int("86086", 15) + x * 15 ** 2
    for a in range(1, 1000000):
        if (m + a) % n == 0:
            c.append(a)
print(min(c))