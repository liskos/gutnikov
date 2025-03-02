x = 9 ** 8 + 3 ** 5 - 2
s = []
while x > 0:
    s = [x % 3] + s
    x //= 3
print(s.count(2))