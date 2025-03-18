import sys

sys.setrecursionlimit(3000)
def f(n):
    if n == 5:
        return 5
    return 5 * n * f(n - 1)

print((f(2077) // 36 - f(2076)) // f(2074))