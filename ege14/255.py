for x in range(2, 11):
    a = 1234
    s = []
    while a > 0:
        s = [a % x] + s
        a //= x
    print(x, sum(s))