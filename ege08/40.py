import itertools


s = set()
for a in itertools.product("ABCX", repeat=5):
    if a[-1] == "X" or "X" not in a:
        s.add(a)
print(len(s))