import itertools


for i, a in enumerate(itertools.product("АКРУ", repeat=5), 1):
    if i == 350:
        print(a)