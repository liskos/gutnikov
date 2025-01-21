def f( n ):
  x = 0
  x += 1
  if n >= 1:
    x += 1
    x += f(n-1)
    x += f(n//3)
  return x


print(f(280))