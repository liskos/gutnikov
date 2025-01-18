import itertools


s = set()
for a in itertools.product("МАРТ", repeat=6):
    if a.count("Р") == 2:
        s.add(a)
print(len(s), s)