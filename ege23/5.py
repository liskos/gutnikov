a = [0] * 26
a[1] = 1
for i in range(1,26):
    if i - 1 > 0:
        a[i] += a[i-1]
    if i % 3 == 0 and i // 3 > 0:
        a[i] += a[i// 3]
    if i % 4 == 0 and i // 4 > 0:
        a[i] += a[i // 4]
print(a[25])