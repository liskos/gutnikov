import itertools


s = set()
for a in itertools.permutations("КРОЙ", r=4):
    if a[0] != "Й" and "ОЙ" not in "".join(a):
        s.add(a)
print(len(s))