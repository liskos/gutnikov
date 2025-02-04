import itertools


for i, a in enumerate(itertools.product("ЬСОНЕ", repeat=5), 1):
    if i == 100:
        print(a)