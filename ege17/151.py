r = []
a = [int(x) for x in open("17data/17-1.txt")]
ok = [x for x in a if x % 10 == 6 and x % 3 == 0]
for i in range(1, len(a) - 1):
    if a[i] in ok or a[i + 1] in ok:
        r.append(a[i:i + 1])
print(len(r), min(r))