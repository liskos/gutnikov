def f(n):
  x = 0
  x += n + 1
  if n > 1:
    x += n * 2
    x += f(n-1)
    x += f(n-3)
  return x


for i in range(0, 100):
    if f(i) > 1000000:
        print(i, f(i))