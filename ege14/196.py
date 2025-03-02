x = 49 ** 13 + 7 ** 33 - 49
s = []
while x > 0:
    s = [x%7] + s
    x //= 7
print(s.count(6))