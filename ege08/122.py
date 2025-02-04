import itertools


s = set()
for a in itertools.permutations("МОЛОКО", r=6):
    s.add(a)
print(len(s))