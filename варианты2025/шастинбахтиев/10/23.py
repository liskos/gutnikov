def f(a,b):
    if a == b:
        return 1
    if a > b:
        return 0
    return f(a + 2,b) + f(a + 3,b) + f(a + 5, b)

print(f(5, 11) * f(11,22) * f(22, 33) * f(33, 37))