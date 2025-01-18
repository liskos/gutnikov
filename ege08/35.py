import itertools


f = 0
s = 0
for i, a in enumerate(itertools.product("ДКМО", repeat=5), 1):
    b = "".join(a)
    if b == "ДОМОК":
        f = i
    if b == "КОМОД":
        s = i
    print(f,s)
print(s - f + 1)