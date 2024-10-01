def f(x):
    a = x % 7
    b = x % 2
    c = x % 5
    return str(a) + str(b) + str(c)


k = 0
print(f(55))
for i in range(10, 100):
    if f(i) == "312":
        k += 1
print(k)