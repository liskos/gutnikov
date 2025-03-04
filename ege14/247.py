for n in range(1,5):
    x = n ** 25 - 2 * n ** 13 + 10
    s = []
    while x > 0:
        s = [x % n] + s
        x //= n
    if sum(s) == 75:
        print(n)