import itertools


s = set()
for a in itertools.product("ГБАИ", repeat=6):
    if a[0] in "АИ" and a[-1] == "Г":
        s.add(a)
print(len(s))