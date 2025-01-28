import itertools


s = set()
for a in itertools.permutations("ШАНЕЛЬ", r=6):
    if a[0] != "Ь" and "ЕАЬ" not in "".join(a):
        s.add(a)
print(len(s))