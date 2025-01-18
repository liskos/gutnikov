import itertools


k = 0
for a in itertools.product("КАТЕР", repeat=3):
    if a.count("А") >= 2:
        k += 1
        print(a)
print(k)