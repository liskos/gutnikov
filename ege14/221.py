x = 2 ** 5 * 3 ** 25
s = []
while x > 0:
    s = [x%3] + s
    x //= 3
print(s.count(0) + s.count(1) + s.count(2))