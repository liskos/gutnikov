a = [0] * 100
a[1] = 1
for i in range(1, 14):
    a[i + 1] += a[i]
    a[i + 2] += a[i]
    a[i * 4] += a[i]
print(a[13])