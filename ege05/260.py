def f(n):
    b = bin(n)[2:]
    i = b.rfind("0")
    if i == -1:
        return -1
    c = b[:i] + b[:2] + b[i + 1:]
    return int(c[::-1], 2)


for i in range(1, 120):
    if f(i) == 123:
        print(i)
