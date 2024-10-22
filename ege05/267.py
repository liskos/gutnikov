def f(n):
    b = bin(n)[2:]
    a = b[1:]
    c = b[0]
    a = a.replace("1", "2")
    a = a.replace("0", "1")
    a = a.replace("2", "0")
    return int(c + a, 2)


for i in range(1, 1000, 2):
    if f(i) > 99:
        print(i)