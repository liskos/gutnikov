a = [0] * 18
a[1] = 1
for i in range(1,18):
    if i - 1 > 0:
        a[i] += a[i-1]
    if i % 2 == 0 and i // 2 > 0:
        a[i] += a[i// 2]
    if i % 4 == 0 and i // 4 > 0:
        a[i] += a[i // 4]
print(a[17])