x = 25 ** 56 + 5 ** 138 - 5
s = []
while x > 0:
    s = [x%5] + s
    x //= 5
print(s.count(4))