r = []
a = [int(x) for x in open("17data/17-3.txt")]
for i in range(1, len(a) - 1):
    if sum(a[i:i + 1]) % 2 == 0 and sum(a[i:i + 1]) % 10 != 6:
        r.append(a[i] * a[i + 1] / 2)
print(len(r), max(r))