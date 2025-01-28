import itertools


for i, a in enumerate(itertools.product("ЕИКНУЧ", repeat=3), 1):
    if a[0] == "К":
        print(i)
        break