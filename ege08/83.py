import itertools


k = 0
for i, a in enumerate(itertools.product("АГИЛМОРТ", repeat=4), 1):
    if a[-2] == "А" and a[-1] == "Л":
        k = i
print(k)