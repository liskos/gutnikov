def f(x):
    a = x % 4
    b = x % 3
    c = x % 2
    return str(a) + str(b) + str(c)


print(f(55))
for i in range(10, 100):
    if f(i) == "220":
        print(i)
