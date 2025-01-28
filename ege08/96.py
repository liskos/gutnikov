import itertools


s = set()
for a in itertools.permutations("КОМБАЙН", r=7):
    if a[0] != "Й" and "АЙ" not in "".join(a):
        s.add(a)
print(len(s))