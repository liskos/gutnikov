x = 18 * 7 ** 108 - 5 * 49 ** 76 + 343 ** 35 - 50
x = abs(x)
a = []
while x > 0:
    a.append(x % 49)
    x //= 49
print(sum(a))