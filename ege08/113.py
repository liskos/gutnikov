import itertools


s = set()
for a in itertools.permutations("ПЕСКАРЬ", r=7):
    b = "".join(a)
    ss = b.replace("Е","0").replace("А","0").replace("Р","0")
    if "Ь0" not in ss and a[0] != "Ь":
        s.add(b)
print(len(s),s)