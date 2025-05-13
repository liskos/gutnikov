a = [int(x) for x in open("17data/17-243.txt")]
r = []
maxi = max([x for x in a if x % 119 == 0])

sr_ar = sum(a) / len(a)
for i in range(len(a) - 2):
    if a[i] < maxi and a[i + 1] < maxi:
        r.append(a[i] + a[i + 1])
print(len(r), max(r))
