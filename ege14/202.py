x = 16 ** 20 + 2 ** 30 - 32
s = []
while x > 0:
    s = [x%4] + s
    x //= 4
print(s.count(3))