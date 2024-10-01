def f(x):
    x = str(x)
    a = int(x[0]) + int(x[2]) + int(x[4])
    b = int(x[1]) + int(x[3])
    v = sorted([a, b])
    return str(v[0]) + str(v[1])


for i in range(10000, 100000):
    if f(i) == "621":
        print(i)
