a = [0] * 50
a[1] = 5
for i in range(1,50):
    if i - 1 > 0:
        a[i] += a[i - 1]
    if i % 3 == 0 and i // 3 > 0:
        a[i] += a[i // 3]
print(a[49])