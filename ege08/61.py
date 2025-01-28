import itertools


s = set()
for a in itertools.product("АБВГДЭЮЯ", repeat=5):
    if (a[-1] in "ЭЮЯ") and (a[0] in "ЭЮЯ") and set(a[1:-1]) <= set("АБВГД"):
        s.add(a)
print(len(s))