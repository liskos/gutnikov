import itertools


d = set()
for a in itertools.product("КОРНЕТ", repeat=5):
    b = "".join(a)
    if a.count("О") <= 1 and a.count("Е") <= 1:
        d.add(b)
print(len(d))