x = 9 ** 7 + 3 ** 8 - 1
s = []
while x > 0:
    s = [x % 3] + s
    x //= 3
print(s.count(0),s.count(1),s.count(2))