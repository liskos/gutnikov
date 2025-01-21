def f(n):
  if n>0:
    return n%10+f(n//10)
  else: return 0


for i in range(0, 10000):
    if f(i) > 32:
        print(i, f(i))
        break