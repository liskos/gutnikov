def f(a, b):
    if a in b:
        return 1
    if a > max(b) or a == 23:
        return 0
    return f(a + 3, b) + f(a + 4, b) + f(a * 2, b)


print(f(11, [50, 51, 52, 53, 54]))