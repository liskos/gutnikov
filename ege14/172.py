x = 9 ** 9 + 3 ** 21 - 7
s = []
while x > 0:
    s = [x % 3] + s
    x //= 3
print(s.count(0))