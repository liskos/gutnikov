x = 4 * 125 ** 4 - 25 ** 4 + 9
s = []
while x > 0:
    s = [x % 5] + s
    x //= 5
print(s.count(4))