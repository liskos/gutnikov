a = [0] * 101
a[0] = 3
a[1] = 3
for i in range(2, 101):
    a[i] = a[i - 1] + 2 * a[i - 2] - 5
print(a[100])