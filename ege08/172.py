import itertools


d = set()
for a in itertools.product("СОЛОВЕЙ", repeat=6):
    b = "".join(a)
    if a[0] != "Й" and a[-1] != "Й" and a.count("Й") <= 1 and ("ЙЕ" not in b) and ("ЕЙ" not in b):
        d.add(b)
print(len(d))