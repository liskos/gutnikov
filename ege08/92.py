import itertools


s = set()
for a in itertools.permutations("МАНОК", r=5):
    if a[0] != "О" and "АО" not in "".join(a):
        s.add(a)
print(len(s))