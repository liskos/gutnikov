import itertools


for i, a in enumerate(itertools.product("АИКМНОРТФ", repeat=6), 1):
    if (a[0] != "А") and (a.count("Р") == 3) and ("И" not in a):
        print(i, a)