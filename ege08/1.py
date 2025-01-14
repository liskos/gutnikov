import itertools

for i, a in enumerate(itertools.product("АОУ",repeat=5), 1):
    s = "".join(a)
    if i == 101:
        print(i, s)