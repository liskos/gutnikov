for x in range(4, 10000):
    a = (88 + 2 * 8 ** x) * 8 ** x + 88 + 8 ** 8
    s = []
    while a > 0:
        s = [a%8] + s
        a //= 8
    print(sum(s))