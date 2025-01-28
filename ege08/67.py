import itertools


s = set()
for a in itertools.product("abcdefghijklmnopqrstuvwxyz", repeat=6):
    if a[0] == a[-1] and a[1] == a[-2] and a[2] == a[-3]:
        s.add(a)
print(len(s), s)