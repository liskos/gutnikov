import itertools


d = set()
for a in itertools.permutations("АРТЁМ", r=5):
    b = "".join(a)
    ss = b.replace("А", "X").replace("Ё", "X")
    if "XX" not in a[:2] or "XX" not in a[-2:]:
        d.add(a)
print(len(d))
