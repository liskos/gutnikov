x = 9 * 123 ** 2053 + 5 * 23 ** 3146 + 91 * 47 ** 5533 + 4099
k = 0
s = []
while x > 0:
    s = [x % 23] + s
    x //= 23
for i in range(len(s)):
    if s[i] > 15:
        k += 1
print(k)