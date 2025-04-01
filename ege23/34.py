def f(a, b):
    if a == b:
        return 1
    if a > 0:
        return 0
    if a % 2 == 0:
        return f(a + 1,b) + f(a * 2,b)
    if a % 2 != 0:
        return f(a + 1,b) + f(a * 2 + 1,b)
print(f(2,16))