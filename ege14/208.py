x = 128 ** 30 + 16 ** 60 - 16
s = []
while x > 0:
    s = [x%8] + s
    x //= 8
print(s.count(7))