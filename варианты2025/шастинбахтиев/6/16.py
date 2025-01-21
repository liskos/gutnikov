import sys


sys.setrecursionlimit(10 ** 6)


def f(n):
    if n < 100:
        return n * n
    else:
        if n % 2 == 0:
            return 0.5 * f(n - 1)
        return 2 * f(n - 1)


print(1000 * f(16384) / f(7777))