r = []
a = [int(x) for x in open("17data/17-1.txt")]
d = [x for x in a if x % 9 == 0]
ok = [x for x in a if int(f"{x:o}") % 10 == 3]
for i in range(1, len(a) - 1):
    if (a[i] in ok and a[i + 1] in d) or (a[i + 1] in ok and a[i] in d):
        r.append(a[i:i + 1])
print(len(r), max(r))