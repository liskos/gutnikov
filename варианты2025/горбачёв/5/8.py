import itertools


for i, a in enumerate(itertools.product("WSDA", repeat=6), 1):
    b = "".join(a)
    if "DD" in b and a.count("S") >= 1 and a[-1] != "W":
        print(i, a)