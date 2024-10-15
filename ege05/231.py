def f(n):
    b = bin(n)[2:]
    b = b + b[-2]
    b = b + b[1]
    return int(b, 2)


print(f(11))
k = 0
for i in range(2, 1000):
    if 150 <= f(i) <= 250:
        print(i)
        k += 1
print(k)