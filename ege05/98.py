def f(n):
    s = str(n)
    a = int(s[0]) * int(s[1])
    b = int(s[1]) * int(s[2])
    v = sorted([a, b])
    return str(v[0]) + str(v[1])


print(f(631))
for i in range(100, 1000):
    if f(i) == '621':
        print(i)