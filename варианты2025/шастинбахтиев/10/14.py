for a in range(1, 100000):
    s = []
    x = 3 ** 10 + 3 ** 7 + 3 ** 3 + 2 - a
    while x > 0:
        s = [x % 3] + s
        x //= 3
    if (s.count(0) == s.count(1)) and (s.count(1) == s.count(2)):
        print(a)
        break