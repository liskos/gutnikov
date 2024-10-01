def f(x):
    s = str(x)
    a = int(s[0]) + int(s[2])
    b = int(s[1]) + int(s[3])
    v = sorted([a, b])
    return str(v[0]) + str(v[1])


print(f(3165))
for i in range(1000, 10000):
    if f(i) == "1113":
        print(i)
        break