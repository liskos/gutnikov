x = 32 ** 30 + 8 ** 60 - 32
s = []
while x > 0:
    s = [x%4] + s
    x //= 4
print(s.count(3))