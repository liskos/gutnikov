def f(x, y):
    if x == y:
        return 1
    if x < y:
        return 0
    if x == 20:
        return 0
    return f(x - 2, y) + f(x - 3, y) + f(int(x ** 0.5), y)

print(f(26,3))