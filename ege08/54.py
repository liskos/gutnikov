import itertools


k = 0
for a in itertools.product("СЛОН", repeat=5):
    if 0 < a.count("О") <= 3:
        k += 1
        print(a)
print(k)