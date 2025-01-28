import itertools


k = 0
for i, a in enumerate(itertools.product("АОУ", repeat=5), 1):
    if a[2] == "У":
        print(i)
        break

