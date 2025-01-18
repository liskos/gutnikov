import itertools


s = set()
for a in itertools.product("КРАНТ", repeat=5):
    if a.count("К") == 2:
        s.add(a)
print(len(s))