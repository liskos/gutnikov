import itertools


s = set()
for a in itertools.product("1234", repeat=5):
    if a[0] != "1" and (a[0] != a[4] and a[1] != a[3]):
        s.add(a)
print(len(s))
