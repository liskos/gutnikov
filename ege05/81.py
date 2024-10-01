def f(x):
    s = str(x)
    a = int(s[0]) + int(s[-1])
    b = int(s[1]) + int(s[2])
    v = sorted([a, b])
    return str(v[1]) + str(v[0])


print(f(2357))
for i in range(1000, 10000):
    if f(i) == '128':
        print(i)
        break
