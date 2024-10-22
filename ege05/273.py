def f(n):
    b = bin(n)[2:]
    if n % 2 == 1:
        b = "1" + b + "0"
    else:
        b = "11" + b + "11"
    return int(b, 2)


print(f(14))
s = []
for i in range(1, 100):
    if f(i) < 126:
        s.append(f(i))
print(max(s))