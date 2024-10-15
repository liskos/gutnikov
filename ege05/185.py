def f(n):
    n -= 1
    b = bin(n)[2:].zfill(8)
    b = b.replace("1", "2").replace("0", "1").replace("2", "0")
    return int(b, 2)


for i in range(1, 256):
    if f(i) == 113:
        print(i)
