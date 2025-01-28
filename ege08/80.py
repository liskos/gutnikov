import itertools


for i, a in enumerate(itertools.product("АВГЕН", repeat=4), 1):
    if "А" not in a:
        print(i)
        break