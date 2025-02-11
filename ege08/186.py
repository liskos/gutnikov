import itertools


d = set()
for a in itertools.product("БАЛОН", repeat=6):
    b = "".join(a)
    if a.count("А") <= 1 and a.count("О") <= 1:
        d.add(b)
print(len(d))