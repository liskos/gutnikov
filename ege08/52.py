import itertools


k = 0
for a in itertools.product("КОМАР", repeat=4):
    if a.count("А") <= 3 or "А" not in a:
        k += 1
        print(a)
print(k)