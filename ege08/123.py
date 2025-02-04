import itertools


s = set()
for a in itertools.permutations("АССАСИН", r=7):
    s.add(a)
print(len(s))