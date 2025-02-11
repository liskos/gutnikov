import itertools


d = set()
for a in itertools.product("БАНКИР", repeat=6):
    b = "".join(a)
    if a.count("А") <= 1 and a.count("И") <= 1:
        d.add(b)
print(len(d))