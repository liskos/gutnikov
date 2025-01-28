import itertools


s = set()
for a in itertools.product("АБВГДЯ", repeat=4):
    if (a[-1] == "Я" or a[0] == "Я" or "Я" not in a) and a.count("Я") <= 1:
        s.add(a)
print(len(s), s)