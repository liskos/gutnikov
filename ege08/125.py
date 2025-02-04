import itertools


s = set()
for a in itertools.permutations("ТРАТАТА", r=7):
    s.add(a)
print(len(s))