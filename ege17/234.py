a = [int(x) for x in open("17data/17-1.txt")]
r = []
sr_ar = sum(a) / len(a)
for i in range(len(a) - 2):
    if (((a[i] < sr_ar) or (a[i + 1] < sr_ar) or (a[i + 2] < sr_ar))
            and "9" in str(a[i]) and "9" in str(a[i + 1]) and "9" in str(a[i + 2])):
        r.append(a[i] + a[i + 1] + a[i + 2])
print(len(r), max(r))
