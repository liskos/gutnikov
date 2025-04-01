a = [0] * 16
a[1] = 1
for i in range(1,16):
    if i - 1 > 0:
        a[i] += a[i-1]
    if i - 3 > 0:
        a[i] += a[i- 3]
    if i % 2 == 0 and i // 2 > 0:
        a[i] += a[i // 2]
print(a[15])