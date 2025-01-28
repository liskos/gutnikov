import itertools


k = 0
for i, a in enumerate(itertools.product("АГИЛМОРТ", repeat=4), 1):
    if a[-2] == "И" and a[-1] == "М":
        k = i
print(k)