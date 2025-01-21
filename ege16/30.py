def f(n):
  x = 0
  x += n * n
  if n > 1:
    x += 2 * n + 1
    x += f(n-2)
    x += f(n//3)
  return x


for i in range(0, 1000):
    if f(i) > 3200000:
        print(i, f(i))
        break