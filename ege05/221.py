def f(n):
    s = str(n)
    s = sorted(s)
    if s[0] != "0":
        max = s[-1] + s[1]
        min = s[0] + s[1]
    else:
        min = s[1] + s[0]
        max = s[-1] + s[1]
    return  int(max) - int(min)


print(f(351))
k = 0
for i in range(900, 1000):
    if f(i) == 70:
        k += 1
print(k)