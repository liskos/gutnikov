x = 3 * 17 ** 777 + 15 * 17 ** 250 - 6 * 17 ** 100 + 2
s = []
while x > 0:
    s = [x % 17] + s
    x //= 17
k = set()
for i in range(len(s)):
    if s[i] % 2 == 0:
        k.add(s[i])
print(len(k))