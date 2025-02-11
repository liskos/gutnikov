import itertools


d = set()
for a in itertools.product("КАЛЬКА", repeat=5):
    b = "".join(a)
    if a.count("А") <= 1:
        d.add(b)
print(len(d))