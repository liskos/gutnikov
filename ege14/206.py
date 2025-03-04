x = 64 ** 150 + 4 ** 300 - 32
s = []
while x > 0:
    s = [x%8] + s
    x //= 8
print(s.count(7))