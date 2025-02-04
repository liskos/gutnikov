import itertools


s = set()
for a in itertools.permutations("АЙСБЕРГ", r=7):
    b = "".join(a)
    ss = b.replace("А","0").replace("Е","0")
    if "Й0" not in ss and a[0] != "Й":
        s.add(b)
print(len(s))