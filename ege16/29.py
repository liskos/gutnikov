def f(n):
  x = 0
  x += n - 5
  if n > 1:
    x += n + 8
    x += f(n-2)
    x += f(n-3)
  return x


for i in range(0, 100):
    if f(i) > 3200000:
        print(i, f(i))
        break