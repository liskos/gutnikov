import itertools


s = set()
for a in itertools.permutations("КАЛИЙ", r=5):
    if a[0] != "Й" and "ИА" not in "".join(a):
        s.add(a)
print(len(s))