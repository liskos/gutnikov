x = 9 ** 8 + 3 ** 25 - 14
s = []
while x > 0:
    s = [x % 3] + s
    x //= 3
print(sum(s))