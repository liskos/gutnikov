import functools
import sys


@functools.lru_cache(None)


def f(n):
    if n < 5:
        return 4 ** 4
    return 4 * f(n - 4) + 4

sys.setrecursionlimit(41000)
print(f(4048) / f(4036))