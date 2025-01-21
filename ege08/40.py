import itertools


s = set()
for a in itertools.product("ABCX", repeat=5):
    if "X" not in a[:-1]:
        s.add(a)
print(len(s))