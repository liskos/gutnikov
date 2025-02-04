import itertools


s = set()
for a in itertools.permutations("РУЛЬКА", r=6):
    b = "".join(a)
    ss = b.replace("У","0").replace("А","0")
    if "0Ь" not in ss and a[0] != "Ь":
        s.add(b)
print(len(s))