import itertools


for i, a in enumerate(itertools.product("АДР", repeat=6), 1):
    if a[0] == "Р":
        print(i)
        break