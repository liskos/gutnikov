import itertools


s = set()
for a in itertools.permutations("ПАНЕЛЬ", r=6):
    if a[0] != "Ь" and "ЕЬ" not in "".join(a):
        s.add(a)
print(len(s))