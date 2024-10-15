def f(n):
    b = bin(n)[2:]
    a = b[1:]
    c = b[0]
    d = a.replace("1", "2")
    d = a.replace("0", "1")
    d = a.replace("2", "0")
    z = c + d
    x = int(z, 2)
    return x + n


print(f(13))