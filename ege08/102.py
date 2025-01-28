import itertools


s = set()
for a in itertools.permutations("НИГРОЛ", r=6):
    if a[0] != "О" and "ОИГ" not in "".join(a):
        s.add(a)
print(len(s))