def f(n):
    a = str(n)
    b = int(a[0]) * int(a[1])
    c = int(a[0]) * int(a[2])
    d = int(a[0]) * int(a[3])
    e = sorted([b, c, d])
    return str(e[1]) + str(e[-1])

print(f(2345))
for i in range(1000, 9999):
    if f(i) == "5472":
        print(i)
        break
