import itertools


for i, a in enumerate(itertools.product("АИОУЭ", repeat=4), 1):
    if "".join(a) == "ИААЭ":
        print(i)
        break