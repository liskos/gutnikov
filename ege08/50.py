import itertools


k = 0
for a in itertools.product("КАТЕР", repeat=4):
    if a.count("Р") >= 2:
        k += 1
        print(a)
print(k)