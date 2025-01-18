import itertools


f = 0
s = 0
for i, a in enumerate(itertools.product("АКРУ", repeat=5), 1):
    b = "".join(a)
    if b == "РУКАА":
        f = i
    if b == "УКАРА":
        s = i
    print(f,s)
print(s - f + 1)