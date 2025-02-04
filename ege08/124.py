import itertools


s = set()
for a in itertools.permutations("ЧИУАУА", r=6):
    s.add(a)
print(len(s))