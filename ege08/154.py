import itertools


s = set()
for a in itertools.product("1234", repeat=5):
    if a[0] != "1" and not (a[0] == a[-1] and a[1] == a[-2]):
        s.add(a)
print(len(s))
