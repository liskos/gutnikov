def f(a, b, k):
    if a == b:
        return 1
    if a < b:
        return 0
    if k < 2:
        return f(a - 2, b, k) + f(a - 3, b, k + 1) + f(a//2, b, k)
    return f(a - 2, b, k) + f(a//2, b, k)
print(f(176, 23, 0))