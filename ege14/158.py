x = 9 ** 20 + 3 ** 60 - 5
s = []
while x > 0:
    s = [x % 3] + s
    x //= 3
print(s.count(2))