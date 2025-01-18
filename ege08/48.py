import itertools


s = set()
for a in itertools.product("БАЛКОН", repeat=5):
    if "Б" in a:
        s.add(a)
        print(a)
print(len(s))