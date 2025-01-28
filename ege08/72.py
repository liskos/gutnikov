import itertools


for i, a in enumerate(itertools.product("АКЛОШ", repeat=4), 1):
    if a[0] == "О":
        print(i)
        break