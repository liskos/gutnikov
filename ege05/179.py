def f(n):
    b = bin(n)[2:].zfill(8)
    b = b.replace("1", "2").replace("0", "1").replace("2", "0")
    return int(b, 2) + 1


print(f(120))