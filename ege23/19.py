def f(a, b):
    if a == b:
        return 1
    if a > b:
        return 0
    x = a
    if x // 10 % 10 < 9:
        x += 10
    return f(a + 1, b) + f(x, b)
print(f(11, 27))