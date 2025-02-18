
a = [int(i) for i in open("17.txt")]
b = []
for i in range(len(a) - 5):
    if (a[i] + a[i + 1] > 0 and a[i + 2] + a[i + 3] > 0 and a[i + 4] + a[i + 5] > 0
            and a[i + 2] + a[i + 3] > a[i] + a[i + 1] and a[i + 2] + a[i + 3] > a[i + 4] + a[i + 5]):
        b.append(a[i + 2] * a[i + 3])
print(len(b), min(b))