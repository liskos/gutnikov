def f(n):
    if n < 15:
        return 4
    if n % 3 == 0:
        return f(2 * n / 3) + n - 1
    return f(n - 1) + 3

for i in range(0,100000):
    if f(i) == 251:
        print(i)