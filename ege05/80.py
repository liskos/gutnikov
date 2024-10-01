def f(x):
    s = str(x)
    a = int(s[0]) + int(s[-1])
    b = int(s[1]) + int(s[2])
    v = sorted([a, b])
    return str(v[0]) + str(v[1])

c = 0
print(f(2357))
for i in range(1000, 10000):
    if f(i) == '815':
        c = i
print(c)
