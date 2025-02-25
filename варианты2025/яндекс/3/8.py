import itertools


d = set()
for a in itertools.permutations("АРТЁМ", r=5):
    if not (a[0] in "АЁ" and a[-1] in "АЁ"):
        d.add(a)
print(len(d))
