a = [int(x) for x in open("17data/17-7.txt")]
r = []
for i in range(len(a) - 1):
    if (a[i] + a[i + 1]) % 3 == 0:
        r.append(a[i])
        r.append(a[i + 1])
print(len(r), max(r))
