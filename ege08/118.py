import itertools


s = set()
for a in itertools.permutations("АВРОРА", r=6):
    b = "".join(a)
    ss = b.replace("А","0").replace("Р", "1")
    if "00" not in ss and "11" not in ss:
        s.add(b)
print(len(s),s)