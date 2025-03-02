x = 125 + 25 ** 3 + 5 ** 9
a = []
while x > 0:
    a = [x%5] + a
    x //= 5
print(a.count(0), a)