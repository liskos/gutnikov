x = 9 ** 14 + 3 ** 18 - 9 ** 5 - 27
s = []
while x > 0:
    s = [x % 3] + s
    x //= 3
print(s.count(2))