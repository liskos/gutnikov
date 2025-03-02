x = 9 ** 22 + 3 ** 66 - 18
s = []
while x > 0:
    s = [x % 3] + s
    x //= 3
print(s.count(2))