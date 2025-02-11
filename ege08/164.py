import itertools


d = set()
for a in itertools.permutations(range(16), r=3):
    print(a)
    if a[0] % 2 != a[1] % 2 and a[1] % 2 != a[2] % 2 and a[0] != 0:
        d.add(a)
print(len(d))