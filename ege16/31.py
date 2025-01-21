def f(n):
  if n>0:
    return n%10*f(n//10)
  else: return 1




for i in range(100, 1000):
    if f(i) > 320:
        print(i, f(i))