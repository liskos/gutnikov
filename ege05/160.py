def f(n):
    b = bin(n)[2:0].zfill(8)
    b = b.replace("1", "2")
    b = b.replace("0", "1")
    b = b.replace("2", "0")
    x = int(b, 2)
    return x - n


for i in range(0, 256):
    if f(i) == -21:
        print(i)