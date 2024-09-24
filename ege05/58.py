def f(x):
    s = str(x)
    a = int(s[0]) + int(s[1])
    b = int(s[2]) + int(s[3])
    m = sorted([a, b])
    return str(m[1]) + str(m[0])


print(f(3165))
for i in range(1000, 10000):
    if f(i) == '1412':
        print(i)
        break