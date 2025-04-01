def f(a, b):
    if a == b:
        return 1
    if a > b:
        return 0
    x = a
    if x // 10 % 10 < 9 and x % 10 < 9:
        x += 11
    elif x // 10 % 10 < 9:
        x += 10
    elif x % 10 < 9:
        x += 1
    return f(x, b) + f(x, b)
print(f(25, 51))