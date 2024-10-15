def f(n):
    b = bin(n)[2:0].zfill(8)
    b = b.replace("1", "2")
    b = b.replace("0", "1")
    b = b.replace("2", "0")
    return int(b, 2) + 1


print(f(95))