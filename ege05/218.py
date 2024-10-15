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
for i in range(300,401):
    if f(i) == 20:
        k += 1
print(k)