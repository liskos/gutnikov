for x in range(1, 10000):
    a = 4 ** 2015 + 2 ** x - 2 ** 2015 + 15
    s = bin(a)
    if s.count("1") == 500:
        print(x)
        break