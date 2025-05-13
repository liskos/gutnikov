a = [int(x) for x in open("17data/17-5.txt")]
r = []
ch = [x for x in a if x % 2 == 0]

for i in range(len(a) - 1):
    if a[i] in ch or a[i + 1] in ch:
        r.append(a[i] + a[i + 1])
print(len(r), max(r))