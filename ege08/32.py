import itertools


s = set()
for a in itertools.product("ABCD", repeat=3):
    b = "".join(a)
    ss = b.replace("ADA", "XXX")
    ss = ss.replace("AD", "XX").replace("DA", "XX")
    if ("A" not in ss) and ("BC" not in b) and ("CB" not in b):
        s.add(b)
print(s)
print(len(s))