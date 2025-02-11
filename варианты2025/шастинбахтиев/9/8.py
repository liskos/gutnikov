import itertools


for i, a in enumerate(itertools.product("ГЕИНРСЯ", repeat=6),1):
    b = "".join(a)
    if "ГИРЯ" in b:
        print(i,b)