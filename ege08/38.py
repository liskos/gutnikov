import itertools


f = 0
s = 0
for i, a in enumerate(itertools.product("АОУ", repeat=5), 1):
    b = "".join(a)
    if b == "УАУАУ":
        f = i
    if b == "ОУОУА":
        s = i
    print(f,s)
print(f - s + 1)