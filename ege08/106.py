import itertools


s = set()
for a in itertools.permutations("НОДА", r=4):
    b = "".join(a)
    ss1 = b.replace("ОА", "XX").replace("АО", "XX").replace("НД", "XX").replace("ДН", "XX")
    if "XX" not in ss1:
        s.add(a)
print(len(s))