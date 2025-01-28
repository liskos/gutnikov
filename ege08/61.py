import itertools


s = set()
for a in itertools.product("АБВГДЭЮЯ", repeat=5):
    if (a[-1] == "Я" or a[-1] == "Э" or a[-1] == "Ю") and (a[0] == "Я" or a[0] == "Э" or a[0] == "Ю"):
        s.add(a)
print(len(s))