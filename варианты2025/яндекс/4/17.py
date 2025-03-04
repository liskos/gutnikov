b =[]
a = [int(x) for x in open("17(1).txt")]
m2025 = min([x for x in a if x % 2025 == 0])
for i in range(len(a)-2):
    if (a[i] % m2025 == 0 or a[i + 1] % m2025 == 0 or a[i + 2] % m2025 == 0) and (100000 <= (a[i] + a[i + 1] + a[i + 2]) < 1000000):
        b.append(a[i] + a[i + 1] + a[i + 2])
print(len(b), max(b))