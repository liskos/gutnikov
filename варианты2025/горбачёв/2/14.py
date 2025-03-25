for x in range(1222):
    n = 4 ** x - 3 ** 331 + 9 ** 17
    s = []
    while n > 0:
        s = [n % 5] + s
        n //= 5
    if s.count(0) == 77:
        print(x)
