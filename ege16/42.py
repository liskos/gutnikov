import functools


@functools.lru_cache(None)
def f(n):
    if n == 1:
        return 1
    return f(n - 1) + 3 * g(n - 1)


@functools.lru_cache(None)
def g(n):
    if n == 1:
        return 1
    return f(n - 1) - 2 * g(n - 1)

print(sum(int(x) for x in str(f(18))))