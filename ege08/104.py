import itertools


s = set()
for a in itertools.permutations("НАДПИСЬ", r=7):
    if a[0] != "Ь" and "ЬИА" not in "".join(a):
        s.add(a)
print(len(s))