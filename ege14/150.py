x = 2 * 9 ** 10 - 3 ** 5 + 5
s = []
while x > 0:
    s = [x % 3] + s
    x //= 3
print(s.count(2))