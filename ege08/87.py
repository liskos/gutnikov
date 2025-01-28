import itertools


k = 0
for i, a in enumerate(itertools.product("ВЕКНО", repeat=5), 1):
    if a.count("Н") == 2 and a.count("К") == 2:
        k = i
print(k)
