import functools


@functools.lru_cache(None)
def f(n):
    if n < 3:
        return n
    elif n > 2 and n % 2 == 1:
        return f(n - 1) + f(n - 2) + 1
    else:
        return  sum(f(i) for i in range(1,n))

print(f(38))