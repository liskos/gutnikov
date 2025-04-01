for x in range(1,3053):
    a = 4 ** 151 + 7 ** 283 + 6 ** 82 - 5 * x
    s = []
    while a > 0:
        s = [a % 8] + s
        a //= 8
    if s.count(1) == 26:
        print(x)