import itertools


s = set()
for a in itertools.permutations("ТАРТАР", r=6):
    s.add(a)
print(len(s))