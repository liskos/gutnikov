import itertools


s = set()
for a in itertools.permutations("КАБИНЕТ", r=7):
    if a[0] != "Б" and "ЕА" not in "".join(a):
        s.add(a)
print(len(s))