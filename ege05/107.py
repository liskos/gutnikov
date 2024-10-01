def f(x):
    a = x % 4
    b = x % 2
    c = x % 3
    return str(a) + str(b) + str(c)


k = 0
print(f(55))
for i in range(10, 100):
    if f(i) == "201":
        k += 1
print(k)