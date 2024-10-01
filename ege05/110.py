def f(x):
    a = x % 2
    b = x % 3
    c = x % 5
    return str(a) + str(b) + str(c)


k = 0
print(f(55))
for i in range(10, 100):
    if f(i) == "122":
        k += 1
print(k)