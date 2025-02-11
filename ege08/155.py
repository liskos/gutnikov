import itertools


for i, a in enumerate(itertools.product("АИОУЭ", repeat=6)):
    if a[0] == "О" and a[-1] == "О":
        print(i, a)
    