import itertools


s = set()
for a in itertools.product("ЖИРАФ", repeat=6):
    if 0 < a.count("А") <= 4:
        s.add(a)
        print(a)
print(len(s))