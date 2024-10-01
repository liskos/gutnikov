def f(x):
    a = x % 4
    b = x % 2
    c = x % 3
    return str(a) + str(b) + str(c)


print(f(55))
for i in range(10, 100):
    if f(i) == "311":
        print(i)
        break