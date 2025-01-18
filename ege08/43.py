import itertools


k = 0
for a in itertools.product("ЛЕТО", repeat=5):
    if "Е" in a:
        k += 1
        print(a)
print(k)