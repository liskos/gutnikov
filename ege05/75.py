def f(x):
    x0 = str(x)[-1]
    x1 = str(x)[1]
    x2 = str(x)[0]
    x0 = int(x0) + 5
    x1 = int(x1) + 6
    x2 = int(x2) + 3
    m = sorted([x0, x1, x2])
    return str(m[0]) + str(m[1]) + str(m[2])



c = 0
for i in range(100, 1000):
    if f(i) == '51014':
        c = i
        print(i)
print(c)
