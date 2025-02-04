import itertools


s = set()
for a in itertools.product("1234", repeat=4):
    if a[0] != "1" and not (a[1] == a[2]):
        s.add(a)
print(len(s))
