import functools


@functools.lru_cache(None)
def f( n ):
  x = 0
  x += 1
  if n >= 1:
    x += 1
    x += f(n-1)
    x += f(n//3)
    x += 1
  return x


print(f(280))