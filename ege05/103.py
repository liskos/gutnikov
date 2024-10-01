def f(x):
    a = x % 4
    b = x % 2
    c = x % 5
    return str(a) + str(b) + str(c)


print(f(55))
for i in range(10, 100):
    if f(i) == "313":
        print(i)
        break