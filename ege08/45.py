import itertools


s = set()
for a in itertools.product("КЛОУН", repeat=5):
    if "У" in a:
        s.add(a)
        print(a)
print(len(s))