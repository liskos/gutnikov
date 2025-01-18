import itertools


s = set()
for a in itertools.product("ТОК", repeat=6):
    if a[0] in "ТК":
        s.add(a)
print(len(s), s)