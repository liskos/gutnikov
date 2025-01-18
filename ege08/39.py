import itertools


s = set()
for a in itertools.product("ABCDX", repeat=4):
    if a.count("X") == 1:
        s.add(a)

print(len(s))