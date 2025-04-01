a = [0] * 21
a[1] = 1
for i in range(2, 21):
    a[i] += a[i - 1]
    if i % 3 == 0:
        a[i] += a[i * 2 // 3]
print(a[20])