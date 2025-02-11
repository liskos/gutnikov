import itertools


d = set()
for a in itertools.product("КАЛИЙ", repeat=6):
    b = "".join(a)
    if a[0] != "Й" and a[-1] != "Й" and a.count("Й") <= 1 and ("ЙИ" not in b) and ("ИЙ" not in b):
        d.add(b)
print(len(d))