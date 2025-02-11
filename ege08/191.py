import itertools


d = set()
for a in itertools.product("САЛЬСА", repeat=6):
    b = "".join(a)
    if a.count("А") <= 1:
        d.add(b)
print(len(d))