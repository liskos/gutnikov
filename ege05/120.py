def f(x):
    s = str(x)
    a = int(s[0]) + int(s[1])
    b = int(s[1]) + int(s[2])
    c = int(s[2]) + int(s[3])
    v = sorted([a, b, c])
    return str(v[2]) + str(v[1])


m = 0
print(f(1284))
for i in range(1000, 10000):
    if f(i) == "129":
        m = i
print(m)