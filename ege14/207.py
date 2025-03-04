x = 32 ** 60 + 4 ** 180 - 128
s = []
while x > 0:
    s = [x%8] + s
    x //= 8
print(s.count(7))