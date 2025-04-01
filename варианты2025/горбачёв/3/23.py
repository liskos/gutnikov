def f(a, b):
    if a == b:
        return 1
    if b > a:
        return 0
    y = f(a - 1,b)
    if a % 2 == 0:
        y  += f(a//2, b)
    if a % 3 == 0:
        y += f(a//3, b)
    return y



print(f(122, 57) * f(57, 11))