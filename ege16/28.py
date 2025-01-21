def f(n):
  x = 0
  x += 2 * n + 1
  if n > 1:
    x += 3 * n - 8
    x += f(n-1)
    x += f(n-4)
  return x


for i in range(0, 100):
    if f(i) > 5000000:
        print(i, f(i))
        break