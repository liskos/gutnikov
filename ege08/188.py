import itertools


d = set()
for a in itertools.product("САКУРА", repeat=5):
    b = "".join(a)
    if a.count("А") <= 1 and a.count("У") <= 1:
        d.add(b)
print(len(d))