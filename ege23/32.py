a = [0] * 21
a[1] = 1
for i in range(1, 21):
    if i - 1 > 0:
        a[i] += a[i - 1]
    if i % 2 == 0 and i // 1.5:
        a[i] += a[i // (3 // 2)]
print(a[20])