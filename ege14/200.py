x = 25 ** 94 + 5 ** 216 - 125
s = []
while x > 0:
    s = [x%5] + s
    x //= 5
print(s.count(4))