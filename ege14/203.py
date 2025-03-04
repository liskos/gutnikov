x = 81 ** 5 + 3 ** 30 - 27
s = []
while x > 0:
    s = [x%9] + s
    x //= 9
print(s.count(8))