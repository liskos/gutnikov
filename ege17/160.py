r = []
a = [int(x) for x in open("17data/17-3.txt")]
for i in range(1, len(a) - 1):
    if sum(a[i:i + 1]) % 7 == 0 and a[i] * a[i + 1] > 0:
        r.append(a[i] * a[i + 1])
print(len(r), min(r))