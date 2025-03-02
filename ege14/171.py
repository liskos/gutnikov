x = 9 ** 7 + 3 ** 21 - 9
s = []
while x > 0:
    s = [x % 3] + s
    x //= 3
print(s.count(0))