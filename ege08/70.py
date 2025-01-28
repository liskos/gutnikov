import itertools


s = set()
for a in itertools.product("АБВГ", repeat=5):
    if "Г" not in a[:-1]:
        s.add(a)
print(len(s), s)