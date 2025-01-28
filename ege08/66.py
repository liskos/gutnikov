import itertools


s = set()
for a in itertools.product("abcdefghijklmnopqrstuvwxyz", repeat=4):
    if a[0] == a[-1] and a[1] == a[2]:
        s.add(a)
print(len(s), s)