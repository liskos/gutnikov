x = 9 ** 5 + 3 ** 25 - 20
s = []
while x > 0:
    s = [x % 3] + s
    x //= 3
print(sum(s))