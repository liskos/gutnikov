import itertools


s = set()
for a in itertools.product("САИ", repeat=6):
    if a[0] in "АИ":
        s.add(a)
print(len(s))