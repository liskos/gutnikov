def f(x, y):
    return (x < A + 2) and (y < A - 3) and (3 * x + y > 66)

k = 0
for A in range(0, 500):
    if all(f(x, y) == 0 for x in range(1, 500) for y in range(1, 500)):
        k += 1
print(k)