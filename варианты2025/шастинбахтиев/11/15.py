def dig(x, y):
    return str(x)[0] == str(y)[0]


for a in range(1, 10000):
    if all(not (not dig(x, 28) and dig(x, 47)) or (x > a - 20) for x in range(1, 300)):
        print(a)