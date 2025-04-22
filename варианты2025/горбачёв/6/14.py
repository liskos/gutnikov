k = 0
x = 9 * 57 ** 2024 + 14 * 13 ** 3059 - 87 * 67 ** 1111 + 2027
s = []
while x > 0:
    s = [x % 36] + s
    x //= 36
for i in range(len(s)):
    if s[i] > 20:
        k += 1
print(k)