import itertools


f = 0
s = 0
for i, a in enumerate(itertools.product("ОПРТ", repeat=5), 1):
    b = "".join(a)
    if b == "ТОПОР":
        f = i
    if b == "РОПОТ":
        s = i
    print(f,s)
print(f - s + 1)