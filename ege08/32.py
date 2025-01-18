import itertools


s = set()
for a in itertools.product("1234", repeat=3):
    b = "".join(a)
    if ("14" in b or "41" in b) and "23" not in b and "32" not in b:
        s.add(a)
        print(s)
print(len(s))