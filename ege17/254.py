a = [int(x) for x in open("17data/17-243.txt")]
r = []
maxi = max([x for x in a if x % 151 == 0])
sr_ar = sum(a) / len(a)
for i in range(len(a) - 2):
    if (a[i] > maxi or a[i + 1] > maxi) and ("3" in hex(a[i])[2:] or "3" in hex(a[i + 1])[2:]):
        r.append(a[i] + a[i + 1])
print(len(r), min(r))
