import itertools


for i, a in enumerate(itertools.product("АОУ", repeat=5), 1):
    b = "".join(a)
    if b == "УАУАУ":
        print(i)
        