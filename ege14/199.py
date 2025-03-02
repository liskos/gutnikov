x = 36 ** 17 + 6 ** 66 - 216
s = []
while x > 0:
    s = [x%6] + s
    x //= 6
print(s.count(5))