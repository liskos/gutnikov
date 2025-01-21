def f(n):
    if n <= 3:
        return n
    elif n % 3 == 0:
        return n ** 3 + f(n - 1)
    elif n % 3 == 1: return 2 * f(n - 5)
    return n * n + f(n - 2)

print(f(100))