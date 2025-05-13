def f(n):
    b = bin(n)[2:]
    if n % 2 == 0:
        b = b.replace("0", "1")
    else:
        b = "1" + b[1:].replace("1", "00")
    return int(b, 2)

s = []
for i in range(1, 10000):
    if f(i) <= 600:
        print(i)
        s.append(i)
print(max(s))