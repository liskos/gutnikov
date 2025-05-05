r = []
a = [int(x) for x in open("17data/17-1.txt")]
d7 = [x for x in a if x % 7 == 0]
nd17 = [x for x in a if x % 17 != 0]
for i in range(1, len(a) - 1):
    if a[i] in d7 and a[i + 1] in nd17:
        r.append(sum(a[i:i + 1]))
print(len(r), min(r))