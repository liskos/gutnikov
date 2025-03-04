x = 5 ** 55 + 5 ** 555 * 555 -5
s = []
while x > 0:
    s = [x%5] + s
    x //= 5
print(len(s), s.count(0) + s.count(1) + s.count(2) + s.count(3) + s.count(4))