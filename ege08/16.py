import itertools


for i, a in enumerate(itertools.product("АКРУ", repeat=5), 1):
    b = "".join(a)
    if b == "УКАРА":
        print(i)