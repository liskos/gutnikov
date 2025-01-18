import itertools


f = 0
s = 0
for i, a in enumerate(itertools.product("АМРТ", repeat=4), 1):
    b = "".join(a)
    if b == "МАРТ":
        f = i
    if b == "РАМТ":
        s = i
    print(f,s)
print(s - f + 1)