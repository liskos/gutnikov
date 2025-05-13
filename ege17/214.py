a = [int(x) for x in open("17data/17-4.txt")]
r = []
sr_ar = sum(a) / len(a)
for i in range(len(a) - 1):
    if (a[i] < sr_ar) and (a[i + 1] < sr_ar) and ((a[i] + a[i + 1]) % 100 == 19):
        r.append(a[i] + a[i + 1])
print(len(r), min(r))
