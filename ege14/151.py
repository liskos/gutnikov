x = 5 * 36 ** 7 + 6 ** 10 - 36
s = []
while x > 0:
    s = [x % 6] + s
    x //= 6
print(s.count(5))