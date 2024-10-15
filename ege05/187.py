def f(n):
    b = bin(n)[2:].zfill(8)
    a = b.rfind("1")
    c = b[:a]
    d = b[a:]
    c = c.replace("1", "2").replace("0", "1").replace("2", "0")
    g = c + d
    return int(g, 2)


print(f(193))