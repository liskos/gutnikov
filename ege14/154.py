x = 4 * 25 ** 4 - 5 ** 4 + 14
s = []
while x > 0:
    s = [x % 5] + s
    x //= 5
print(sum(s))