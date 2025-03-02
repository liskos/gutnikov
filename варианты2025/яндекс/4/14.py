for x in range(401, 1000):
    a = 16 ** 560 + 16 ** 120 - x
    b = hex(a)[2:]
    if b.count("0") == 442:
        print(x)