
a = [int(x) for x in open("17data/17-294.txt")]
r = []
sr_ar = sum(a) / len(a)
for i in range(len(a) - 1):
    s = sum(map(int, str(a[i]))) + sum(map(int, str(a[i + 1])))
    if int(s ** 0.5)**2 == s and a[i]  + a[i + 1] > sr_ar:
        r.append(s)
print(len(r), max(r))
