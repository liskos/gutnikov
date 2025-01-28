import itertools


s = set()
for a in itertools.product("АБВГДЕ", repeat=4):
    if a.count("Г") == 1 and (a[0] == "Г" or a[-1] == "Г"):
        s.add(a)
print(len(s), s)