def f(x):
    b = bin(x)[2:]
    if b.count('1') % 2 == 0:
        b = b + '1'
        b += '1'
    else:
        b = b + '0'
        b += '0'
    return int(b, 2)

a = []
for i in range(1, 100):
    if f(i) > 54:
        a.append(f(i))
print(min(a))