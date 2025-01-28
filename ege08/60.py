import itertools


s = set()
for a in itertools.product("АБВГЭЮЯ", repeat=5):
    if (a[-1] in "ЭЮЯ") and (a[0] in "ЭЮЯ") and set(a[1:-1]) <= set("АБВГ"):
        s.add(a)
print(len(s))