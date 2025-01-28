import itertools


k = 0
for i, a in enumerate(itertools.product("ВЕКНО", repeat=5), 1):
    if a.count("О") == 1 and a.count("Е") == 1:
        k = i
print(k)
