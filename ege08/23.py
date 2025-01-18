import itertools


s = set()
for a in itertools.product("КОТ", repeat=6):
    if a.count("К") == 2:
        s.add(a)
print(len(s))