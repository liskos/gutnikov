def f(n):
    b = bin(n)[2:]
    if n % 2 == 0:
        b = b.replace("0", "1")
    else:
        b = "1" + b[1:].replace("1", "00")
    return int(b, 2)

print(f(11)==32)
s = []
for i in range(1, 10000):
    if f(i) <= 600:
        s.append([i, f(i)])
s.sort(reverse=True, key=lambda x:(x[1], x[0]))
print(s)