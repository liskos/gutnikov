a = [0] * 20
a[1] = 1
for i in range(2, 20):
    a[i] = 2 * a[i-1] + i + 3
print(a[19])
print(a)