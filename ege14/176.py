x = 9 ** 17 + 3 ** 16 - 27
s = []
while x > 0:
    s = [x % 3] + s
    x //= 3
print(s.count(0),s.count(1),s.count(2))