def f(x):
    return not (x & a == 0) or ((x & 77 == 0) and (x & 44 == 0))


for a in range(10000):
    if all(f(x) for x in range(10000)):
        print(a)
        break