x = 2 ** 102 + 2 ** 100 + 2 ** 85 + 2 ** 17
s = []
while x > 0:
    s = [x%8] + s
    x //= 8
print(len(set(s)))