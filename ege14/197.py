x = 64 ** 115 + 8 ** 305 - 512
s = []
while x > 0:
    s = [x%8] + s
    x //= 8
print(s.count(7))