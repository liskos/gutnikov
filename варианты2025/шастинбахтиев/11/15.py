def dig(x, y):
    if x[0] == y[0]:
        return x, y
for a in range(1, 10000):
    if all((not (dig(x, 28)) and (not (dig(x, 47)) or (x > a - 20))) for x in range(1, 300) for y in range(1, 300)):
        print(a)