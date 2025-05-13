a = [int(x) for x in open("17.txt")]
k = 0
for i in range(len(a) - 2):
    if (a[i] * a[i + 1] * a[i + 2]) % 10 == (max(a[i: i + 3])) % 10:
