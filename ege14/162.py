x = 9 ** 8 + 3 ** 24 - 6
s = []
while x > 0:
    s = [x % 3] + s
    x //= 3
print(s.count(2))