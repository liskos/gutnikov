x = 36 ** 10 + 6 ** 25 - 15
s = []
while x > 0:
    s = [x%6] + s
    x //= 6
print(s.count(0))