def f(x):
    s = str(x)
    a = int(s[0]) + int(s[1])
    b = int(s[1]) + int(s[2])
    v = sorted([a, b])
    return str(v[0]) + str(v[1])


k = 0
print(f(843))
for i in range(100, 1000):
    if f(i) == '1216':
        k += 1
print(k)