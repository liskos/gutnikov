import itertools


s = set()
for a in itertools.product("КОТ", repeat=5):
    if a.count("О") == 2:
        s.add(a)
print(len(s))