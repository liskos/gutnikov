import itertools

for i, a in enumerate(itertools.product("АОУ", repeat=5), 1):
    if a[0] in "О":
        print(i)
