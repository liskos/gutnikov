import itertools

for k in range(1,20):
    s = 0
    for i in itertools.product("01", repeat=20):
        if i.count("0") == k:
            s += 1
    print(k, s)
