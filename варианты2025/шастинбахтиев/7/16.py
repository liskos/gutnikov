import functools
import sys


sys.setrecursionlimit(10 ** 6)
@functools.lru_cache(None)
def f(n):
    if n > 7000:
        return n + 4
    return 3 * n + 5 + f(n + 3)

for i in range(7000, 706, -1):
    f(i)

print(f(707) - f(716))