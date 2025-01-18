import itertools


k = 0
for a in itertools.product("БАЛКОН", repeat=3):
    if "Б" in a:
        k += 1
        print(a)
print(k)