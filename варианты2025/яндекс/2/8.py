import itertools


apt = 0
pch = 0
for i, a in enumerate(itertools.product("АЕКПТЧ", repeat=7), 1):
    b = "".join(a)
    if b == "АПТЕЧКА":
        apt = i
    if b == "ПЕЧАТКА":
        pch = i
print(apt, pch, (pch - apt) - 1)