import itertools


s = set()
for a in itertools.permutations("1234", r=4):
    s.add(a)
print(len(s))