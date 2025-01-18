import itertools


s = set()
for a in itertools.product("ЛЕТО", repeat=4):
    if a[0] in "ЛТ":
        s.add(a)
print(len(s))