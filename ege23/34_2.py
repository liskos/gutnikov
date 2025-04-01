a = [0] * 21
a[2] = 1
for i in range(3,17):
    if i % 2 == 0:
        a[i] += a[i - 1] + a[i // 2]
    else:
        a[i] += a[i - 1] + a[(i - 1) //2]
print(a[16])