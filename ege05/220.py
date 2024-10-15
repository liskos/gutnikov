def f(n):
    s = str(n)
    s = sorted(s)
    max1 = s[-1] + s[1]
    if s[0] != "0":
        min1 = s[0] + s[1]
    elif s[1] != "0":
        min1 = s[1] + "0"
    else:
        min1 = max1
    return  int(max1) - int(min1)


print(f(351))
k = 0
for i in range(700, 801):
    if f(i) == 80:
        k += 1
print(k)