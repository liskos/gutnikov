import sys
sys.setrecursionlimit(60000)

def f(n):
    if n < 222:
        return 111
    return 2 * (n + 4) + f(n - 3)


print(f(55555) - f(55543))