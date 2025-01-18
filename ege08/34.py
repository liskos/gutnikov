import itertools


f = 0
s = 0
for i, a in enumerate(itertools.product("АЗНС", repeat=5), 1):
    b = "".join(a)
    if b == "САЗАН":
        f = i
    if b == "ЗАНАС":
        s = i
    print(f,s)
print(f - s + 1)