x = 64 ** 30 + 2 ** 300 - 32
s = []
while x > 0:
    s = [x%4] + s
    x //= 4
print(s.count(3))